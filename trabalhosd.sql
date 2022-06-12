create database if not exists Livraria;
use Livraria;

create table Autor(
id_autor int not null primary key,
first_name varchar(40),
middle_name varchar(40),
last_name varchar(40),
area_interest varchar(40),
acronym varchar(10));


create table Livro(
isbn int,
price int, 
titulo varchar(40),
autor_id int,
foreign key (autor_id) references Autor(id_autor)
);

-- adicionar autores
Insert into Autor (id_autor,first_name,middle_name,last_name,area_interest,acronym)
values(1,"Kenny","Rogger","Afonso","Ciencia","KAfonso"),
(2,"Bruno","Angelo","Jesus","Tecnologias","Astro"),
(3,"Joelson","Adolfo","Spinola","Desing","JS");
-- adicionar livros
insert into Livro(isbn,price,titulo,autor_id)values
(101,300,"AI",1),
(121,3200,"ArquiteturaPC",2),
(101,200,"ReactJS",3);
-- adicionar novos livros
insert into Livro(isbn,price,titulo,autor_id)values(1010,2000,"AI Vol2",1);

-- eliminar livros relacionados a um determinado autor
delete Livro from Livro
inner join Autor
on (Livro.autor_id)=(Autor.id_autor)
where id=1;

-- informacao sobre todos os livros de um autor
select titulo as Nome_Livro,price as Preco,isbn as ISBN,first_name as Primeiro_Nome,last_name as Ultimo_Nome from Livro
inner join Autor
on (Livro.autor_id)=(Autor.id_autor)
where id =1;

-- selecionar o livro de menor valor
select titulo, price from Livro
where price=(select MIN(price) from Livro);

-- selecionar o livro de maior valor
select titulo, price from Livro
where price=(select MAX(price) from Livro);

-- quantos livros estao na livraria
select count(titulo) from Livro;

-- cd to book shop
create table Artist(
id_Artist int not null primary key,
first_name varchar(40),
middle_name varchar(40),
last_name varchar(40),
artistic_name varchar(20),
city varchar(30),
bithdate date);


create table CD_DVD( 
titulo_album varchar(40),
genero varchar(30),
ano_lancamento date,
numero_disco int,
duracao time,
artist_id int,
preco_album int,
foreign key (artist_id) references Artist(id_Artist)
);
-- add artistas and cds
insert into Artist(id_Artist,first_name,middle_name,last_name,artistic_name,city,bithdate) 
values (1,"Eva","Lima","David","ED","Mindelo",'2000-02-11'),
(2,"Mark","Delman","Tavares","Mark Delman","Mindelo",'1992-02-11'),
(3,"Queren","Patricia","Cruz","Lil Software","Mindelo",'2001-05-30');


insert into CD_DVD(titulo_album,genero,ano_lancamento,numero_disco,duracao,preco_album,artist_id)
values("Era Uma vez","R&B",'2025-03-12',"01",'00:40:20',300,1),
("5AM","Rap&R&B",'2019-12-06',"02",'00:50:20',200,2),
("SomeOne","R&B",'2025-04-30',"01",'01:20:20',600,3);

-- eliminr cd de um determinado artista
delete CD_DVD from CD_DVD
inner join Artist
on (CD_DVD.artist_id)=(Artist.id_Artist)
where id_Artist=2;

-- informacao sobre todos os CD_DVD de um Artista
select titulo_album as Nome,genero as Genero_Musical,ano_lancamento as Ano,numero_disco as Numero,duracao as Tempo,
first_name as Primeiro_Nome,last_name as Apelido from CD_DVD
inner join Artist
on (CD_DVD.artist_id)=(Artist.id_Artist)
where id_Artist=3;

-- selecionar o CD_DVD de menor valor
select titulo_album, preco_album from CD_DVD
where preco_album=(select MIN(preco_album) from CD_DVD);

-- selecionar o CD_DVD de maior valor
select titulo_album, preco_album from CD_DVD
where preco_album=(select MAX(preco_album) from CD_DVD);

-- quantos CD_DVD estao na livraria
select count(titulo_album) from CD_DVD;

