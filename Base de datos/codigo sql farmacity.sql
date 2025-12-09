create table Medicamentos(
id_medicamentos int auto_increment primary key,
nombre varchar(30),
categoria varchar(50),
precio decimal(10,2),
stock int
);
create table Ventas(
id_venta int auto_increment primary key,
id_medicamento int,
fecha date,
cantidad int,
foreign key (id_medicamento) references Medicamentos(id_medicamento)
);
insert into Medicamentos(nombre, categoria, precio, stock)
values 
('Ibuprofeno','Analgesico',5000.00,50),
('Tafirol','Antibiotico',4500.00,70),
('Buscapina','Anticolinergico',7400.00,95);

insert into Ventas(id_medicamento, fecha, cantidad)
values
(1,'25-3-2025',5),
(2,'5-5-2025',7),
(1,'8-12-2025',4);











;