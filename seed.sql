-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS peluqueria_usuarios;
USE peluqueria_usuarios;


-- Tabla de usuarios
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100),
    email VARCHAR(100) NOT NULL UNIQUE,
    telefono VARCHAR(20)
);

-- Tabla de estados para las citas
CREATE TABLE estados_cita (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE,
    descripcion TEXT
);

-- Tabla de citas
CREATE TABLE citas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT NOT NULL,
    peluquero_id INT NOT NULL,
    estado_id INT NOT NULL,
    fecha DATETIME NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES usuarios(id),
    FOREIGN KEY (peluquero_id) REFERENCES usuarios(id),
    FOREIGN KEY (estado_id) REFERENCES estados_cita(id)
);


-- Lista de estado para las citas
INSERT INTO estados_cita (nombre, descripcion) VALUES
('pendiente', 'La cita ha sido creada pero no confirmada'),
('confirmada', 'La cita ha sido confirmada'),
('cancelada', 'La cita fue cancelada'),
('completada', 'La cita ha sido realizada');

-- Usuarios Admin
INSERT INTO usuarios (nombre, apellido, email, telefono) VALUES
('Laura', 'Martínez', 'laura.admin@peluqueria.com', '1234567890');

-- Usuarios Peluqueros
INSERT INTO usuarios (nombre, apellido, email, telefono) VALUES
('Carlos', 'Pérez', 'carlos.p@peluqueria.com', '1234567891'),
('María', 'López', 'maria.l@peluqueria.com', '1234567892');

-- Usuarios Clientes
INSERT INTO usuarios (nombre, apellido, email, telefono) VALUES
('Juan', 'Ramírez', 'juan.ramirez@email.com', '1234567893'),
('Ana', 'Torres', 'ana.torres@email.com', '1234567894');

-- Usuarios Citas
INSERT INTO citas (cliente_id, peluquero_id, estado_id, fecha) VALUES
(4, 2, 1, '2025-10-10 15:00:00'),
(5, 3, 2, '2025-10-11 11:30:00');