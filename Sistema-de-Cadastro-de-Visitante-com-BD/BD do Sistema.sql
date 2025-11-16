create database if not exists sistema_visitantes;
use sistema_visitantes;

create table if not exists visitantes (
id int auto_increment primary key,
nome varchar(100) not null,
documento varchar(14) not null,
visitado varchar(100) not null,
motivo varchar(200),
entrada datetime not null,
saida datetime
)default charset=utf8;

select * from visitantes;
