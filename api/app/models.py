from flask_sqlalchemy import SQLAlchemy


# Se genera la clase que permite la interaccion con la base de datos
db = SQLAlchemy()


# Tabla de roles
class Rol(db.Model):


    # Especifico el nombre de la tabla
    __tablename__ = 'roles_usuario'


    # Defino los valores que tiene la tabla
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)


    # Defino las relaciones entre tablas
    usuarios = db.relationship('Usuario', backref='rol', lazy=True)


# Tabla de usuarios
class Usuario(db.Model):


    # Especifico el nombre de la tabla
    __tablename__ = 'usuarios'


    # Defino los valores que tiene la tabla
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True, nullable=False)
    telefono = db.Column(db.String(20))
    password_hash = db.Column(db.String(255), nullable=False)
    fecha_registro = db.Column(db.DateTime, server_default=db.func.now())
    activo = db.Column(db.Boolean, default=True)
    rol_id = db.Column(db.Integer, db.ForeignKey('roles_usuario.id'), nullable=False)

    # Defino las relaciones entre tablas
    citas_como_cliente = db.relationship('Cita', foreign_keys='Cita.cliente_id', backref='cliente', lazy=True)
    citas_como_peluquero = db.relationship('Cita', foreign_keys='Cita.peluquero_id', backref='peluquero', lazy=True)


    # Funcion que devuelve el contenido en un diccionario
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'telefono': self.telefono,
            'rol': self.rol.nombre if self.rol else None,
        }


# Tabla de estados de citas
class EstadoCita(db.Model):


    # Especifico el nombre de la tabla
    __tablename__ = 'estados_cita'
    

    # Defino los valores que tiene la tabla
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    descripcion = db.Column(db.Text)


    # Defino las relaciones entre tablas
    citas = db.relationship('Cita', backref='estado', lazy=True)


# Tabla de citas
class Cita(db.Model):


    # Especifico el nombre de la tabla
    __tablename__ = 'citas'


    # Defino los valores que tiene la tabla
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    peluquero_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    estado_id = db.Column(db.Integer, db.ForeignKey('estados_cita.id'), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)


    # Funcion que devuelve el contenido en un diccionario
    def to_dict(self):
        return {
            'id': self.id,
            'cliente': self.cliente.to_dict(),
            'peluquero': self.peluquero.to_dict(),
            'estado': self.estado.nombre,
            'fecha': self.fecha.isoformat()
        }
