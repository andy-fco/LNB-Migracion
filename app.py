from flask import Flask, abort, flash, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import (
    LoginManager, UserMixin, login_user,
    logout_user, login_required, current_user
)
import requests

from models import (
    db, User, Equipo, Jugador, Articulo, Evento,
    EventoAficionado, AficionadoJugador, DT
)

def normalizar_posicion(pos):
    pos = pos.lower()

    if "base" in pos:
        return "Base"
    if "escolta" in pos:
        return "Escolta"
    if "alero" in pos:
        return "Alero"
    if "ala" in pos:
        return "Ala-Pivot"
    if "pivot" in pos:
        return "Pivot"

    return None


app = Flask(__name__)
app.config["SECRET_KEY"] = "clave_secreta_123"


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lnb.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
bcrypt = Bcrypt(app)



login_manager = LoginManager(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


#------------ RUTAS ---------------

@app.route("/")
def index():
    try:
        gnews_api_key = "b6e169c2ada7c7fba93403ff919b77f9"
        url = f"https://gnews.io/api/v4/search?q=basquet&lang=es&country=ar&max=6&apikey={gnews_api_key}"
        r = requests.get(url, timeout=6)
        r.raise_for_status()
        data = r.json()
        articles = data.get("articles", [])
    except Exception as e:
        articles = []
        error = f"Error obteniendo noticias: {e}"
        return render_template("index.html", articles=articles, error=error)
    return render_template("index.html", articles=articles, error=None)

#EQUIPOS 
@app.route("/equipos")
def equipos():
    all_equipos = Equipo.query.all()
    return render_template("equipos.html", equipos=all_equipos)


@app.route("/equipo/<int:id>")
def equipo_detalle(id):
    equipo = Equipo.query.get_or_404(id)
    jugadores = Jugador.query.filter_by(equipo_id=id).all()
    dts = DT.query.filter_by(equipo_id=id).all()
    return render_template("equipo_detalle.html", equipo=equipo, jugadores=jugadores, dts=dts)

#JUGADORES
@app.route("/jugador/<int:id>")
def jugador_detalle(id):
    jugador = Jugador.query.get_or_404(id)
    return render_template("jugador_detalle.html", jugador=jugador)

#NOVEDADES 

#EVENTSO
@app.route("/eventos")
def eventos():
    lista = Evento.query.order_by(Evento.fecha_y_hora.asc()).all()
    return render_template("eventos.html", eventos=lista)

@app.route("/eventos/<int:id>")
def evento_detalle(id):
    evento = Evento.query.get_or_404(id)
    inscriptos = EventoAficionado.query.filter_by(evento_id=id).count()

    ya_inscripto = False
    if current_user.is_authenticated:
        ya_inscripto = EventoAficionado.query.filter_by(
            evento_id=id,
            aficionado_id=current_user.id
        ).first() is not None

    return render_template("evento_detalle.html",
                           evento=evento,
                           inscriptos=inscriptos,
                           ya_inscripto=ya_inscripto)

@app.route("/eventos/<int:id>/inscribirse")
@login_required
def evento_inscribir(id):
    evento = Evento.query.get_or_404(id)

    inscriptos = EventoAficionado.query.filter_by(evento_id=id).count()
    if inscriptos >= evento.cap_max:
        return "No quedan más cupos."

    ya = EventoAficionado.query.filter_by(
        evento_id=id,
        aficionado_id=current_user.id
    ).first()

    if not ya:
        ins = EventoAficionado(evento_id=id, aficionado_id=current_user.id)
        db.session.add(ins)
        db.session.commit()

    return redirect(url_for("evento_detalle", id=id))

#NOTICIAS
@app.route("/noticias")
def noticias():
    articulos = Articulo.query.order_by(Articulo.fecha.desc()).all()
    return render_template("noticias.html", articulos=articulos)

@app.route("/noticias/<int:id>")
def noticia_detalle(id):
    articulo = Articulo.query.get_or_404(id)
    return render_template("noticia_detalle.html", articulo=articulo)

#JUEGOS

@app.route("/juegos")
@login_required
def juegos():
    return render_template("juegos.html")

#MI JUGADOR

@app.route("/mi_jugador/crear", methods=["GET", "POST"])
@login_required
def crear_mi_jugador():

    
    existente = Jugador.query.filter_by(aficionado_id=current_user.id).first()
    if existente:
        flash("Ya creaste tu jugador. Si querés modificarlo, debés eliminarlo y crearlo de nuevo.", "warning")
        return redirect(url_for("mi_jugador"))

    if request.method == "POST":

        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        ciudad = request.form["ciudad"]
        nacionalidad = request.form["nacionalidad"]
        altura = float(request.form["altura"])
        camiseta = int(request.form["camiseta"])
        posicion = request.form["posicion"]
        mano_habil = request.form["mano_habil"]
        especialidad = request.form["especialidad"]
        jugada = request.form["jugada"]

        stats = {
            "tiro": 65,
            "pase": 65,
            "dribling": 65,
            "velocidad": 65,
            "defensa": 65,
            "salto": 65
        }
 
        bonus_esp = {
            "Tiro": {"tiro": 3, "dribling": 1, "velocidad": 1},
            "Asistencias": {"pase": 3, "dribling": 1, "velocidad": 1},
            "Volcadas": {"salto": 3, "velocidad": 2},
            "Tapas": {"defensa": 3, "salto": 2},
            "Uno contra uno": {"dribling": 3, "velocidad": 2},
            "Defensa": {"defensa": 3, "velocidad": 1, "salto": 1},
            "Poste bajo": {"defensa": 2, "salto": 2},
        }

        if especialidad in bonus_esp:
            for stat, inc in bonus_esp[especialidad].items():
                stats[stat] += inc
 
        bonus_jugada = {
            "Alley-oop": {"pase": 1, "salto": 2},
            "Volcada": {"salto": 2},
            "Volcada en transición": {"velocidad": 2},
            "Triple": {"tiro": 2},
            "Salida de tirador": {"tiro": 2},
            "Stepback": {"tiro": 2, "dribling": 1},
            "Flotadora": {"tiro": 1, "dribling": 1},
            "Gancho": {"tiro": 1, "defensa": 1},
            "Cross-over": {"dribling": 2},
            "Pick n roll": {"pase": 1, "velocidad": 1},
            "Pick n pop": {"tiro": 2},
            "No-look pass": {"pase": 2},
        }

        if jugada in bonus_jugada:
            for stat, inc in bonus_jugada[jugada].items():
                stats[stat] += inc
 
        media = round(sum(stats.values()) / len(stats))
 
        nuevo = Jugador(
            nombre=nombre,
            apellido=apellido,
            ciudad=ciudad,
            nacionalidad=nacionalidad,
            altura=altura,
            camiseta=camiseta,
            posicion=posicion,
            mano_habil=mano_habil,
            especialidad=especialidad,
            jugada=jugada,
            tiro=stats["tiro"],
            pase=stats["pase"],
            dribling=stats["dribling"],
            velocidad=stats["velocidad"],
            defensa=stats["defensa"],
            salto=stats["salto"],
            media=media,
            equipo_id=None,   
            aficionado_id=current_user.id
        )

        db.session.add(nuevo)
        db.session.commit()

        flash("¡Jugador creado con éxito!", "success")
        return redirect(url_for("mi_jugador"))

     
    return render_template("mi_jugador_crear.html")



@app.route("/mi_jugador")
@login_required
def mi_jugador():
    jugador = Jugador.query.filter_by(aficionado_id=current_user.id).first()
    return render_template("mi_jugador.html", jugador=jugador)

# PERFIL
@app.route("/perfil")
@login_required
def perfil():
    user = current_user

    jugador_fav = user.jugador_favorito
    equipo_fav = user.equipo_favorito

    relaciones = (
        AficionadoJugador.query
        .filter_by(aficionado_id=user.id)
        .join(Jugador, AficionadoJugador.jugador_id == Jugador.id)
        .all()
    )

    def posicion_principal(pos):
        if not pos:
            return None
        return pos.split("/")[0].strip()  

    quinteto = {
        "Base": None,
        "Escolta": None,
        "Alero": None,
        "Ala-Pivot": None,
        "Pivot": None,
    }

    for rel in relaciones:
        pos = posicion_principal(rel.jugador.posicion)
        if pos in quinteto:
            quinteto[pos] = rel.jugador

    eventos_inscripto = (
        EventoAficionado.query
        .filter_by(aficionado_id=user.id)
        .join(Evento, EventoAficionado.evento_id == Evento.id)
        .all()
    )

    return render_template(
        "perfil.html",
        user=user,
        jugador_fav=jugador_fav,
        equipo_fav=equipo_fav,
        quinteto=quinteto,
        eventos_inscripto=eventos_inscripto,
    )


@app.route("/perfil/elegir-equipo")
@login_required
def elegir_equipo():
    equipos = Equipo.query.all()
    return render_template("elegir_equipo.html", equipos=equipos)


@app.route("/perfil/guardar-equipo/<int:id>")
@login_required
def guardar_equipo(id):
    equipo = Equipo.query.get_or_404(id)
    current_user.equipo_favorito_id = equipo.id
    db.session.commit()
    flash("Equipo favorito actualizado.", "success")
    return redirect(url_for("perfil"))


@app.route("/perfil/elegir-jugador")
@login_required
def elegir_jugador():
    jugadores = Jugador.query.filter_by(aficionado_id=None).all()
    return render_template("elegir_jugador.html", jugadores=jugadores)


@app.route("/perfil/guardar-jugador/<int:id>")
@login_required
def guardar_jugador(id):
    jugador = Jugador.query.get_or_404(id)
    current_user.jugador_favorito_id = jugador.id
    db.session.commit()
    flash("Jugador favorito actualizado.", "success")
    return redirect(url_for("perfil"))


@app.route("/quinteto/<posicion>")
@login_required
def editar_quinteto(posicion):

    posiciones_validas = ["Base", "Escolta", "Alero", "Ala-Pivot", "Pivot"]
    if posicion not in posiciones_validas:
        abort(404)

    
    def posicion_principal(pos):
        if not pos:
            return None
        return pos.split("/")[0].strip()

    
    jugadores = [
        j for j in Jugador.query.filter_by(aficionado_id=None).all()
        if posicion_principal(j.posicion) == posicion
    ]

    return render_template("quinteto_elegir.html",
                           posicion=posicion,
                           jugadores=jugadores)


@app.route("/quinteto/guardar/<posicion>/<int:jugador_id>")
@login_required
def guardar_quinteto(posicion, jugador_id):

    posiciones_validas = ["Base", "Escolta", "Alero", "Ala-Pivot", "Pivot"]
    if posicion not in posiciones_validas:
        abort(404)

    
    def posicion_principal(pos):
        if not pos:
            return None
        return pos.split("/")[0].strip()

    relaciones = (
        AficionadoJugador.query
        .filter_by(aficionado_id=current_user.id)
        .join(Jugador)
        .all()
    )

    for rel in relaciones:
        if posicion_principal(rel.jugador.posicion) == posicion:
            db.session.delete(rel)

    nueva = AficionadoJugador(
        aficionado_id=current_user.id,
        jugador_id=jugador_id
    )
    db.session.add(nueva)
    db.session.commit()

    flash(f"{posicion} actualizado.", "success")
    return redirect(url_for("perfil"))




@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        mail = request.form["mail"]

        hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")

        user = User(
            username=username,
            password=hashed_pw,
            mail=mail,
            role="aficionado"
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("login"))

    return render_template('register.html')




@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("index"))
        else:
            flash("Credenciales inválidas", "danger")
            return redirect(url_for("login"))

    return render_template("login.html")





# --------- INICIALIZAR ---------

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
