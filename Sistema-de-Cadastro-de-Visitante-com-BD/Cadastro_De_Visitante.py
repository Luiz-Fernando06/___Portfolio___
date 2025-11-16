# bibliotecas
from datetime import datetime  # Biblioteca para data(horario)
from time import sleep
import mysql.connector

#--------------------------
#CONFIGURAÇÂO DO BANCO DE DADOS
#--------------------------
def conectar():
    '''Conectar ao SGBD MySQL'''
    return mysql.connector.connect(
        host = 'localhost',
        user='root',
        password='',
        database='sistema_visitantes'
    )


# -------------------------
# Funções auxiliares
# -------------------------

# Função para formatar e validar CPF
def formatar_e_validar_cpf(cpf: str) -> str | None:
    """Remove formatação e valida CPF. Retorna o CPF limpo se for válido, senão None."""
    cpf = ''.join(filter(str.isdigit, cpf))  # Remove tudo que não for número

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return None

    # Validação do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto

    # Validação do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto

    if cpf[-2:] != f"{digito1}{digito2}":
        return None

    return cpf


# -------------------------
# Funções principais
# -------------------------

# Função para registar entrada do visitante
def registrar_entrada():
    """Registra a entrada de um visitante."""
    print("\n=== Registrar Entrada ===")

    '''
    Aqui estou criando uma variavel para inserir seu nome e evitando espaços
    desnecessarios, e verificando se o valor logico da minha variavel for False
     exibir uma mensagem "O nome é obrigatorio" e retorna para o menu
     '''
    nome = input("Nome (*obrigatorio): ").strip()
    if not nome:
        print("O nome é obrigatório.\n")
        return


    '''
    Aqui esta acontecendo uma validação de CPF que foi feita na função 
    "formatar_e_validar_cpf", onde crio a variavel "documento", elimino 
    espaços desnecessarios e chamo a função de validação para verificar se
    o documento digitado é um CPF valido, e caso o valor logico seja False
    ou o CPF for invalido, exiba "CPF invalido!" e retorne para o menu
    '''
    documento = input('CPF: ').strip()
    documento = formatar_e_validar_cpf(documento)
    if not documento:
        print('CPF inválido!\n')
        return


    '''
    Aqui eu crio uma variavel chamada "visitado" para inserir quem você veio 
    visitar, eliminando espaços desnecessarios e caso o valor logico fo False, 
    então exibir "Campo visitado obrigatorio", e retorne ao menu
    '''
    visitado = input('Quem é a pessoa que veio visitar: ').strip()
    if not visitado:
        print("Campo 'visitado' obrigatório.\n")
        return


    '''
    Aqui eu crio a variavel "motivo" para insirir o motivo da visita e
    eliminar os espaços desnecessarios
    '''
    motivo = input('Motivo da visita: ').strip()


    '''
    Aqui eu salvo essa variavel "entada" com o metodo datetime.now()
    da biblioteca datetime, para pegar a data e o horario em tempo real
    '''
    entrada = datetime.now()

    try:
        '''
        Aqui estou tentando abrir uma conexão com o banco de dados usando 
        uma função chamada conectar()
        '''
        con = conectar()


        '''
        Cria um cursor: objeto usado para executar comandos SQL.
        O parâmetro "dictionary=True" faz com que os resultados 
        sejam retornados como dicionários Python em vez de tuplas.
        '''
        cur = con.cursor(dictionary=True)


        '''
        Executa uma consulta SQL procurando por um visitante com 
        o mesmo documento e cuja saída ainda não foi registrada 
        (ou seja, ainda está dentro).
        '''
        cur.execute("SELECT * FROM visitantes WHERE documento=%s AND saida IS NULL", (documento,))


        '''
        Usa fetchone() para pegar o primeiro resultado.
        Se encontrar algo -> significa que esse visitante já está dentro do prédio.
        Então o código avisa e sai da função com return'''
        if cur.fetchone():
            print("Este visitante já está dentro!\n")
            return


        '''
        Caso o visitante não esteja dentro, insere um novo registro na tabela 
        visitantes com os dados informados.
        '''
        cur.execute("""
                    INSERT INTO visitantes (nome, documento, visitado, motivo, entrada)
                    VALUES (%s, %s, %s, %s, %s)
                """, (nome, documento, visitado, motivo, entrada))


        '''
        Confirma (grava) as mudanças no banco de dados.
        Sem isso, o INSERT ficaria apenas em memória.
            '''
        con.commit()


        '''
        Mostra uma mensagem confirmando que a entrada foi registrada, 
        com a data/hora formatada.
        '''
        print(f"Entrada registrada para {nome} às {entrada.strftime('%d/%m/%Y %H:%M:%S')}.\n")


        '''
        Se ocorrer qualquer erro durante o processo 
        (como problema de conexão ou SQL inválido), ele é 
        capturado e exibido.
        '''
        '''
        Fecha a conexão com o banco de dados — mesmo que tenha dado erro.
        Isso é importante para evitar conexões abertas.
        '''
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        con.close()


# Função para registrar a saída do visitante
def registrar_saida():
    """Registra a saída de um visitante."""
    print("\n=== Registrar Saída ===")

    '''
    Aqui eu escrevo meu CPF eliminando espaços desnecessarios e caso vc
    escreve um cpf que não esta no BD ou clique em enter vai exibir 
    "CPF inválido!" e retorna para o menu
    '''
    documento = input("CPF do visitante: ").strip()
    if not documento:
        print('CPF inválido!\n')
        return


    '''
    Aqui estou pegando a data e o horario em tempo real
    '''
    saida = datetime.now()


    try:
        '''
        Aqui eu me conecto ao BD novamente crio um cursor para executar comando e
        varifico se o CPF diigitado é um CPF existente no BD e pula para o proximo
        bloco de comando, agr se o valor logico for False vai exibir "Visitante não
        encontrado ou já saiu" e retorna para o menu
        '''
        con = conectar()
        cur = con.cursor(dictionary=True)
        cur.execute("SELECT * FROM visitantes WHERE documento=%s AND saida IS NULL", (documento,))
        v = cur.fetchone()
        if not v:
            print("Visitante não encontado ou já saiu.\n")
            return


        '''
        Aqui estou modificando minha saida para registrar a
        SAIDA em tempo real, atraves do id do proprio BD e depois 
        gravando a SAIDA no BD
        '''
        cur.execute("UPDATE visitantes SET saida=%s WHERE id=%s", (saida, v['id']))
        con.commit()
        print(f"Saída registrada para {v['nome']} às {saida.strftime('%d/%m/%Y %H:%M:%S')}.\n")


    #Aqui estou fazendo o controle de exceções e fechando a conexão com o BD
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        con.close()


# Função para listar todos os registros
def listar_visitante():
    '''Listar visitantes'''
    print("\n=== Lista de Visitantes ===\n")

    try:
        con = conectar()
        cur = con.cursor(dictionary=True)

        '''Aqui estou ordenando a tabela por ordem crescente pelo nome'''
        cur.execute("SELECT * FROM visitantes ORDER BY nome")


        '''
        Pega todas as linhas restantes do último comando SELECT executado.
        Retorna uma lista de resultados (geralmente listas de tuplas ou 
        listas de dicionários se dictionary=True foi usado).
        '''
        visitantes = cur.fetchall()

        #Se não tiver visitantes para listar
        if not visitantes:
            print("Nenhum visitante encontrado.\n")
            return

        #Amostra todo os valores da minha coluna
        for v in visitantes:
            print(f"ID: {v['id']}\nNome: {v['nome']}\nCPF: {v['documento']}\nVisitado: {v['visitado']}\n"
                  f"Motivo: {v['motivo']}\nEntrada: {v['entrada']}\nSaída: {v['saida']}\n")

    #Controle de exceções e fim da conecção com o BD
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        con.close()


# Função para buscar um visitante especifico
def buscar_visitante():
    """Busca visitante pelo nome ou CPF."""
    print("\n=== Buscar Visitante ===")
    termo = input("Digite o nome ou CPF: ").strip()

    try:
        con = conectar()
        cur = con.cursor(dictionary=True)

        '''
        Aqui estou selecionando meus valores pelo nome ou CPF
        '''
        cur.execute("""
                SELECT * FROM visitantes
                WHERE nome LIKE %s OR documento=%s
            """, (f"%{termo}%", termo))
        resultados = cur.fetchall() #Aqui estou listando

        #Caso não encontre os dados no BD
        if not resultados:
            print("Nenhum visitante encontrado.\n")
            return

        #Caso encontre, liste todos eles
        for v in resultados:
            print(f"\nID: {v['id']}\nNome: {v['nome']}\nCPF: {v['documento']}\nVisitado: {v['visitado']}\n"
                  f"Motivo: {v['motivo']}\nEntrada: {v['entrada']}\nSaída: {v['saida']}\n")

    #Exceções e Fim de conexão
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        con.close()

def atualizar_registro():
    """Atualiza informações de um visitante pelo CPF."""
    print("\n=== Atualizar Registro ===")

    documento = input("CPF do visitante que deseja atualizar: ").strip()
    if not documento:
        print("CPF inválido!\n")
        return

    try:
        con = conectar()
        cur = con.cursor(dictionary=True)

        # Busca o visitante pelo CPF
        cur.execute("SELECT * FROM visitantes WHERE documento = %s ORDER BY id DESC LIMIT 1", (documento,))
        visitante = cur.fetchone()

        if not visitante:
            print("Visitante não encontrado.\n")
            return

        print("\nPressione ENTER para manter o valor atual.\n")

        # Solicita novos valores (mantém os antigos se nada for digitado)
        novo_nome = input(f"Nome atual [{visitante['nome']}]: ").strip() or visitante['nome']
        novo_visitado = input(f"Visitado atual [{visitante['visitado']}]: ").strip() or visitante['visitado']
        novo_motivo = input(f"Motivo atual [{visitante['motivo']}]: ").strip() or visitante['motivo']

        cur.execute("""
            UPDATE visitantes
            SET nome = %s, visitado = %s, motivo = %s
            WHERE id = %s
        """, (novo_nome, novo_visitado, novo_motivo, visitante['id']))
        con.commit()

        print("\nRegistro atualizado com sucesso!\n")

    except Exception as e:
        print(f"Erro ao atualizar: {e}\n")
    finally:
        con.close()

# Função para remover um registro
def remove_registro():
    print("\n=== Remover Registro ===")
    documento = input("CPF do visitante: ").strip()
    documento = formatar_e_validar_cpf(documento)
    if not documento:
        print("CPF inválido!\n")
        return

    try:
        con = conectar()
        cur = con.cursor()

        #Deletando o registro
        cur.execute("DELETE FROM visitantes WHERE documento=%s", (documento,))
        con.commit()
        print("Registro removido.\n")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        con.close()


# -------------------------
# Função principal (menu)
# -------------------------

def main():
    while True:
        print("=" * 40)
        print(f"{'Sistema de cadastro de visitante':^40}")
        print("=" * 40)
        print("\n1 - Registrar entrada"
              "\n2 - Registrar saída"
              "\n3 - Listar visitantes"
              "\n4 - Buscar visitante"
              "\n5 - Remover registro"
              "\n6 - Atualizar registro"
              "\n0 - Sair")
        opcao = input("Escolha uma opção: \n").strip()

        try:
            if opcao == '1':
                registrar_entrada()

            elif opcao == '2':
                registrar_saida()

            elif opcao == '3':
                listar_visitante()

            elif opcao == '4':
                buscar_visitante()

            elif opcao == '5':
                remove_registro()

            elif opcao == '6':
                atualizar_registro()

            elif opcao == '0':
                print("Saindo", end="")
                sleep(0.5)
                print(end='.')
                sleep(1)
                print(end=".")
                sleep(1)
                print(end=".")
                sleep(2)
                print("\n>Sistema finalizado<\n")
                break

            else:
                print("Opção inválida.\n")
        except KeyboardInterrupt:
            print("\nInterrupção detectada. Voltando ao menu...\n")
        except Exception as e:
            print(f"Erro inesperado: {e}\n")


# -------------------------
# Executa o programa
# -------------------------
if __name__ == "__main__":
    main()
