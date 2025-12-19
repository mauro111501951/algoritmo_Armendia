DROP DATABASE IF EXISTS escuela;
CREATE DATABASE escuela;
USE escuela;

CREATE TABLE Rubricas (
    id_rubrica INT PRIMARY KEY AUTO_INCREMENT,
    nombre_rubrica VARCHAR(40)
);

CREATE TABLE Criterios (
    id_criterio INT PRIMARY KEY AUTO_INCREMENT,
    nombre_criterio VARCHAR(40),
    nota FLOAT,
    nota_maxima INT,
    rubrica INT,
    FOREIGN KEY (rubrica) REFERENCES Rubricas(id_rubrica)
);