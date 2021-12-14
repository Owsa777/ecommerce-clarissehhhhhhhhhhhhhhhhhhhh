CREATE TABLE Categoria
(
    id integer NOT NULL,
   	nombre varchar(20) NOT NULL,
	descripcion varchar(200),
	PRIMARY KEY(id)
)

CREATE TABLE Producto
(
    id integer NOT NULL,
    id_categoria integer NOT NULL,
    precio numeric NOT NULL,
	descripcion varchar(200) NOT NULL,
	imagen integer NOT NULL,
	nombre varchar(100),
	PRIMARY KEY(id),
	FOREIGN KEY(id_categoria) REFERENCES Categoria(id)
)

CREATE TABLE Talla
(
    id integer NOT NULL,
    id_producto integer NOT NULL,
    stock integer,
	descripcion varchar(10) NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(id_producto) REFERENCES Producto(id)
)

CREATE TABLE Usuario
(
    id integer NOT NULL,
    email varchar(100) NOT NULL,
    password varchar(200) NOT NULL,
	nombre varchar(50) NOT NULL,
	apellidos varchar(100) NOT NULL,
	telefono varchar(10),
	id_direccionp integer,
	PRIMARY KEY(id)
)

CREATE TABLE Direccion
(
    id integer NOT NULL,
    id_usuario integer NOT NULL,
    calle varchar(100) NOT NULL,
	ciudad varchar(100) NOT NULL,
	estado varchar(100) NOT NULL,
	codigo_postal varchar(10),
	PRIMARY KEY(id),
	FOREIGN KEY(id_usuario) REFERENCES Usuario(id)
)

CREATE TABLE Tipo_Pago
(
    id integer NOT NULL,
    nombre integer NOT NULL,
    imagen integer NOT NULL,
	PRIMARY KEY(id)
)

CREATE TABLE Pago
(
    id integer NOT NULL,
    id_usuario integer NOT NULL,
    id_tipo integer NOT NULL,
	  PRIMARY KEY(id),
	FOREIGN KEY(id_usuario) REFERENCES Usuario(id),
	FOREIGN KEY(id_tipo) REFERENCES Tipo_Pago(id)
)

CREATE TABLE Paqueteria
(
    id integer NOT NULL,
    nombre varchar(100) NOT NULL,
    imagen integer NOT NULL,
	PRIMARY KEY(id)
)

CREATE TABLE Orden
(
    id integer NOT NULL,
    id_usuario integer NOT NULL,
    id_pago integer NOT NULL,
	id_paqueteria int(30),
	total numeric NOT NULL,
	direccion varchar(200) NOT NULL,
	fecha date NOT NULL,
	estatus boolean NOT NULL,
	clave_rastreo varchar(100),
	PRIMARY KEY(id),
	FOREIGN KEY(id_usuario) REFERENCES Usuario(id),
	FOREIGN KEY(id_pago) REFERENCES Pago(id),
	FOREIGN KEY(id_paqueteria) REFERENCES Paqueteria(id)
)

CREATE TABLE Carrito
(
    id integer NOT NULL,
    id_usuario integer NOT NULL,
    id_producto integer NOT NULL,
	id_talla integer NOT NULL,
	cantidad integer NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(id_usuario) REFERENCES Usuario(id),
	FOREIGN KEY(id_producto) REFERENCES Producto(id),
	FOREIGN KEY(id_talla) REFERENCES Talla(id)
)

CREATE TABLE Ordenado
(
    id integer NOT NULL,
    id_orden integer NOT NULL,
    id_producto integer NOT NULL,
	id_talla integer NOT NULL,
	cantidad integer NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(id_orden) REFERENCES Orden(id),
	FOREIGN KEY(id_producto) REFERENCES Producto(id),
	FOREIGN KEY(id_talla) REFERENCES Talla(id)
)
