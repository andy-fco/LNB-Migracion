from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

# =====================================================
#  USER (Agrupa administradores + aficionados)
# =====================================================
class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(20), default="aficionado")   # admin | aficionado

    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    mail = db.Column(db.String(200), unique=True, nullable=False)

    # Datos personales
    nombre = db.Column(db.String(20))
    apellido = db.Column(db.String(30))
    fecha_nacimiento = db.Column(db.Date)
    puntos = db.Column(db.Integer, default=0)

    # Perfil
    foto_perfil = db.Column(db.String(300))

    # Favoritos
    equipo_favorito_id = db.Column(db.Integer, db.ForeignKey("equipos.id"))
    jugador_favorito_id = db.Column(db.Integer, db.ForeignKey("jugadores.id"))

    equipo_favorito = db.relationship("Equipo", foreign_keys=[equipo_favorito_id])
    jugador_favorito = db.relationship("Jugador", foreign_keys=[jugador_favorito_id])

    # Quinteto ideal (N*M)
    quinteto = db.relationship("AficionadoJugador", back_populates="aficionado")


# =====================================================
#  EQUIPOS
# =====================================================
class Equipo(db.Model):
    __tablename__ = "equipos"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), unique=True)
    ciudad = db.Column(db.String(50))
    estadio = db.Column(db.String(50))
    fecha_fundacion = db.Column(db.Date)
    temporadas = db.Column(db.Integer)
    campeonatos = db.Column(db.Integer)

    escudo = db.Column(db.String(300))
    foto_estadio = db.Column(db.String(300))

    jugadores = db.relationship("Jugador", back_populates="equipo_rel")
    dts = db.relationship("DT", back_populates="equipo_rel")


# =====================================================
#  DIRECTORES TÉCNICOS
# =====================================================
class DT(db.Model):
    __tablename__ = "dts"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20))
    apellido = db.Column(db.String(30))
    fecha_nacimiento = db.Column(db.Date)
    nacionalidad = db.Column(db.String(30))
    ciudad = db.Column(db.String(50))

    equipo_id = db.Column(db.Integer, db.ForeignKey("equipos.id"))
    temporadas = db.Column(db.Integer)

    foto = db.Column(db.String(300))

    equipo_rel = db.relationship("Equipo", back_populates="dts")


# =====================================================
#  JUGADORES (Incluye cartas creadas por usuarios)
# =====================================================
class Jugador(db.Model):
    __tablename__ = "jugadores"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20))
    apellido = db.Column(db.String(30))
    camiseta = db.Column(db.Integer)
    media = db.Column(db.Integer)
    posicion = db.Column(db.String(15))
    nacionalidad = db.Column(db.String(30))

    equipo_id = db.Column(db.Integer, db.ForeignKey("equipos.id"))
    equipo_rel = db.relationship("Equipo", back_populates="jugadores")

    # Stats
    tiro = db.Column(db.Integer)
    dribling = db.Column(db.Integer)
    velocidad = db.Column(db.Integer)
    pase = db.Column(db.Integer)
    defensa = db.Column(db.Integer)
    salto = db.Column(db.Integer)

    # Datos extra
    fecha_nacimiento = db.Column(db.Date)
    ciudad = db.Column(db.String(50))
    altura = db.Column(db.Float)
    mano_habil = db.Column(db.String(10))
    especialidad = db.Column(db.String(30))
    jugada = db.Column(db.String(30))

    # Si este jugador pertenece a la carta de un aficionado:
    aficionado_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    foto_carnet = db.Column(db.String(300))
    media_day = db.Column(db.String(300))
    foto_juego = db.Column(db.String(300))


# =====================================================
#  QUINTETO IDEAL
# =====================================================
class AficionadoJugador(db.Model):
    __tablename__ = "aficionado_jugador"

    id = db.Column(db.Integer, primary_key=True)

    aficionado_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    jugador_id = db.Column(db.Integer, db.ForeignKey("jugadores.id"))

    aficionado = db.relationship("User", back_populates="quinteto")
    jugador = db.relationship("Jugador")


# =====================================================
#  ARTÍCULOS
# =====================================================
class Articulo(db.Model):
    __tablename__ = "articulos"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), unique=True)
    descripcion = db.Column(db.String(3000))
    fecha = db.Column(db.Date)

    portada = db.Column(db.String(300))
    foto_1 = db.Column(db.String(300))
    foto_2 = db.Column(db.String(300))
    foto_3 = db.Column(db.String(300))


# =====================================================
#  EVENTOS
# =====================================================
class Evento(db.Model):
    __tablename__ = "eventos"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), unique=True)
    descripcion = db.Column(db.String(3000))
    fecha_y_hora = db.Column(db.DateTime)
    cap_max = db.Column(db.Integer)

    portada = db.Column(db.String(300))
    foto_1 = db.Column(db.String(300))

    inscriptos = db.relationship("EventoAficionado", back_populates="evento")


# =====================================================
#  INSCRIPCIÓN A EVENTOS
# =====================================================
class EventoAficionado(db.Model):
    __tablename__ = "evento_aficionado"

    id = db.Column(db.Integer, primary_key=True)

    evento_id = db.Column(db.Integer, db.ForeignKey("eventos.id"))
    aficionado_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    evento = db.relationship("Evento", back_populates="inscriptos")
    aficionado = db.relationship("User")
