import re
import os
from datetime import datetime, date
from app import app, db
from models import User, Equipo, Jugador, DT, Articulo, Evento, AficionadoJugador, EventoAficionado

SQL_FILE = "lnb.sql"

# ============================================================
# PARSER SEGURO PARA VALORES DE INSERT
# ============================================================

def parse_values(raw):
    """
    Convierte una línea del tipo:
    (1, 'Andrés', 'Fernandez', NULL, '2002-09-26', '')

    en una lista de Python bien separada.
    """
    vals = []
    current = ""
    inside_quotes = False

    for c in raw:
        if c == "'" and inside_quotes:
            inside_quotes = False
            current += c
        elif c == "'" and not inside_quotes:
            inside_quotes = True
            current += c
        elif c == "," and not inside_quotes:
            vals.append(current.strip())
            current = ""
        else:
            current += c

    if current:
        vals.append(current.strip())

    # limpiar comillas y convertir tipos
    clean_vals = []
    for v in vals:
        if v.upper() == "NULL":
            clean_vals.append(None)
        elif v.startswith("'") and v.endswith("'"):
            clean_vals.append(v[1:-1])
        else:
            # número o fecha
            clean_vals.append(v)

    return clean_vals


def sql_date(v):
    if v is None:
        return None
    try:
        return datetime.strptime(v, "%Y-%m-%d").date()
    except:
        return None


def sql_datetime(v):
    if v is None:
        return None
    try:
        return datetime.strptime(v, "%Y-%m-%d %H:%M:%S")
    except:
        return None


# ============================================================
# INSERT FUNCTIONS FOR EACH TABLE
# ============================================================

def insert_administrador(v):
    """
    administradores:
    id, nombre, apellido, id_usuario, pass
    → User(role='admin')
    """
    user = User(
        id=int(v[0]),
        role="admin",
        nombre=v[1],
        apellido=v[2],
        username=v[3],
        password=v[4],   # ya viene cifrada en tu SQL original
        mail=f"{v[3]}@admin.fake",  # porque SQL NO trae email
    )
    db.session.merge(user)


def insert_aficionado(v):
    """
    aficionados:
    id, nombre, apellido, id_usuario, pass, email, d_of_birth,
    equipo_favorito, jugador_favorito, puntos, foto_perfil(BLOB)
    """
    user = User(
        id=int(v[0]),
        role="aficionado",
        nombre=v[1],
        apellido=v[2],
        username=v[3],
        password=v[4],
        mail=v[5],
        fecha_nacimiento=sql_date(v[6]),
        equipo_favorito_id=int(v[7]) if v[7] else None,
        jugador_favorito_id=int(v[8]) if v[8] else None,
        puntos=int(v[9]) if v[9] else 0,
        foto_perfil=None
    )
    db.session.merge(user)


def insert_equipo(v):
    obj = Equipo(
        id=int(v[0]),
        nombre=v[1],
        ciudad=v[2],
        estadio=v[3],
        fecha_fundacion=sql_date(v[4]),
        temporadas=int(v[5]) if v[5] else None,
        campeonatos=int(v[6]) if v[6] else None,
        escudo=None,
        foto_estadio=None,
    )
    db.session.merge(obj)


def insert_dt(v):
    obj = DT(
        id=int(v[0]),
        nombre=v[1],
        apellido=v[2],
        fecha_nacimiento=sql_date(v[3]),
        nacionalidad=v[4],
        ciudad=v[5],
        equipo_id=int(v[6]) if v[6] else None,
        temporadas=int(v[7]) if v[7] else None,
        foto=None
    )
    db.session.merge(obj)


def insert_jugador(v):
    obj = Jugador(
        id=int(v[0]),
        nombre=v[1],
        apellido=v[2],
        camiseta=int(v[3]) if v[3] else None,
        media=int(v[4]) if v[4] else None,
        posicion=v[5],
        nacionalidad=v[6],
        equipo_id=int(v[7]) if v[7] else None,
        tiro=int(v[8]) if v[8] else None,
        dribling=int(v[9]) if v[9] else None,
        velocidad=int(v[10]) if v[10] else None,
        pase=int(v[11]) if v[11] else None,
        defensa=int(v[12]) if v[12] else None,
        salto=int(v[13]) if v[13] else None,
        fecha_nacimiento=sql_date(v[14]),
        ciudad=v[15],
        altura=float(v[16]) if v[16] else None,
        mano_habil=v[17],
        especialidad=v[18],
        jugada=v[19],
        aficionado_id=int(v[20]) if v[20] else None,
        foto_carnet=None,
        media_day=None,
        foto_juego=None
    )
    db.session.merge(obj)


def insert_articulo(v):
    obj = Articulo(
        id=int(v[0]),
        titulo=v[1],
        descripcion=v[2],
        fecha=sql_date(v[3]),
        portada=None,
        foto_1=None,
        foto_2=None,
        foto_3=None,
    )
    db.session.merge(obj)


def insert_evento(v):
    obj = Evento(
        id=int(v[0]),
        titulo=v[1],
        descripcion=v[2],
        fecha_y_hora=sql_datetime(v[3]),
        cap_max=int(v[4]) if v[4] else None,
        portada=None,
        foto_1=None,
    )
    db.session.merge(obj)


def insert_evento_aficionado(v):
    obj = EventoAficionado(
        id=int(v[0]),
        evento_id=int(v[1]),
        aficionado_id=int(v[2]),
    )
    db.session.merge(obj)


def insert_aficionado_jugador(v):
    obj = AficionadoJugador(
        id=int(v[0]),
        aficionado_id=int(v[1]),
        jugador_id=int(v[2])
    )
    db.session.merge(obj)


# ============================================================
# TABLE ROUTER
# ============================================================

TABLE_MAP = {
    "administradores": insert_administrador,
    "aficionados": insert_aficionado,
    "equipos": insert_equipo,
    "dts": insert_dt,
    "jugadores": insert_jugador,
    "articulos": insert_articulo,
    "eventos": insert_evento,
    "evento_aficionado": insert_evento_aficionado,
    "aficionado_jugador": insert_aficionado_jugador,
}


# ============================================================
# MAIN IMPORTER
# ============================================================

print("▶ Borrando y recreando tablas…")

with app.app_context():
    db.drop_all()
    db.create_all()

print("▶ Leyendo archivo SQL…")

with open(SQL_FILE, encoding="utf-8") as f:
    sql = f.read()

# Encontrar TODOS los INSERTS con su bloque completo de valores
inserts = re.findall(
    r"INSERT INTO\s+`(\w+)`\s+\([^\)]*\)\s+VALUES\s*(.*?);",
    sql,
    flags=re.DOTALL | re.IGNORECASE
)


print(f"▶ {len(inserts)} inserts encontrados.")

print(f"▶ {len(inserts)} inserts encontrados.")

with app.app_context():
    for table, values_block in inserts:
        if table not in TABLE_MAP:
            continue

        print(f"➡ Procesando tabla: {table}")

        # Separa filas del VALUES
        rows = re.findall(r"\((.*?)\)", values_block, flags=re.DOTALL)

        for raw_row in rows:
            vals = parse_values(raw_row)
            TABLE_MAP[table](vals)

    print("▶ Guardando en DB…")
    db.session.commit()


print("✔ Importación completa.")
