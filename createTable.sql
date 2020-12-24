 use datarepresentation
 
  create table books(
    -> id int NOT NULL auto_increment,
    -> title varchar(255),
    -> author varchar(255),
    -> ISBN int,
    -> price int,
    -> PRIMARY KEY (id)
    -> );