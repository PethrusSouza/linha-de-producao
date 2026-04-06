create table cad_itens(
nome varchar (100) not null,
P_12 int (10),
descricao_item varchar (300) not null,
medidas enum ('BL', 'TL', 'M²', 'CM'),
acabamento varchar (300) not null
);