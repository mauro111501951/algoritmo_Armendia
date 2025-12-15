drop database if exists farmacity;
create database farmacity;
use farmacity;

create table medicamentos (
    id_medicamentos int auto_increment primary key,
    nombre varchar(30),
    categoria varchar(50),
    precio decimal(10,2),
    stock int
);

create table ventas (
    id_venta int auto_increment primary key,
    id_medicamento int,
    fecha date,
    cantidad int,
    foreign key (id_medicamento)references medicamentos(id_medicamentos)
);

insert into medicamentos (nombre, categoria, precio, stock)
values
('ibuprofeno', 'analgesico', 5000.00, 50),
('tafirol', 'analgesico', 4500.00, 70),
('buscapina', 'anticolinergico', 7000.00, 95);

insert into ventas (id_medicamento, fecha, cantidad)
values
(1, '2025-3-25', 5),
(2, '2025-5-5', 7),
(1, '2025-12-8', 4);












;
