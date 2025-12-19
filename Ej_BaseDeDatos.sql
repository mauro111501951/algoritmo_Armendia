DROP DATABASE IF EXISTS mortalkombat;
CREATE DATABASE mortalkombat;
USE mortalkombat;

-- TABLA DE RAZAS
CREATE TABLE razas (
    id_raza INT AUTO_INCREMENT PRIMARY KEY,
    nombre_raza VARCHAR(50)
);

-- TABLA DE HABILIDADES ESPECIALES
CREATE TABLE habilidades (
    id_habilidad INT AUTO_INCREMENT PRIMARY KEY,
    nombre_habilidad VARCHAR(50)
);

-- TABLA DE PERSONAJES
CREATE TABLE personajes (
    id_personaje INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    poder INT,
    raza INT,
    habilidad INT,
    FOREIGN KEY (raza) REFERENCES razas(id_raza),
    FOREIGN KEY (habilidad) REFERENCES habilidades(id_habilidad)
);

-- INSERTAR RAZAS
INSERT INTO razas (nombre_raza) VALUES
("Earthrealm"),
("Outworld"),
("Netherrealm"),
("Edenia"),
("Chaosrealm"),
("Orderrealm");

-- INSERTAR HABILIDADES
INSERT INTO habilidades (nombre_habilidad) VALUES
("Hielo Criomante"),
("Fuego Espiritual"),
("Magia Oscura"),
("Teletransportación"),
("Artes Marciales Shaolin"),
("Fuerza Sobrehumana"),
("Control del Viento"),
("Magia Edeniana");

-- INSERTAR PERSONAJES INICIALES
INSERT INTO personajes (nombre, poder, raza, habilidad) VALUES
("Scorpion", 9500, 3, 2),       -- Netherrealm + fuego espiritual
("Sub-Zero", 9000, 1, 1),       -- Earthrealm + hielo
("Liu Kang", 9800, 1, 5),       -- Earthrealm + artes shaolin
("Kitana", 8600, 4, 8),         -- Edenia + magia edeniana
("Raiden", 9900, 1, 7),         -- Earthrealm + control del viento/tormentas
("Mileena", 8700, 2, 6);        -- Outworld + fuerza sobrehumana
