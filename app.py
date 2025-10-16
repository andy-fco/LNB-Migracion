
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import (
    LoginManager, UserMixin, login_user,
    logout_user, login_required, current_user
)
import requests

app = Flask(__name__)
app.config["SECRET_KEY"] = "clave_secreta_123" 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

gnews_api_key = "b6e169c2ada7c7fba93403ff919b77f9"

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"  


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    mail = db.Column(db.String(200), unique=True, nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def index():
    try:
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

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        mail = request.form["mail"]
        hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")
        user = User(username=username, password=hashed_pw , mail = mail)
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
            login_user(user)  # Crea la sesión
            return redirect(url_for("index"))
        else:
            return "Credenciales inválidas"

    return render_template('login.html')

@app.route("/equipos")
def equipos():
    return render_template("equipos.html")

@app.route("/noticias")
def noticias():
    return render_template("noticias.html")

@app.route("/eventos")
def eventos():
    return render_template("eventos.html")

@app.route("/juegos")
@login_required
def juegos():
    return render_template("juegos.html")

@app.route("/mi_jugador")
@login_required
def mi_jugador():
    return render_template("mi_jugador.html")

@app.route("/perfil")
@login_required
def perfil():

    return render_template("perfil.html", username = current_user.username , mail = current_user.mail)



@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
