from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    foto = None
    nome = None

    fotos = {
        "gustavo": "gustavo.jpg",
        "richard": "richard.jpg",
        "matheus": "matheus.jpg",
        "miguel": "miguel.jpg",
        "jose": "jose.jpg"
    }

    if request.method == "POST":

        nome = request.form["nome"]

        nome_minusculo = nome.lower()

        if nome_minusculo in fotos:
            foto = fotos[nome_minusculo]

    return render_template(
        "index.html",
        foto=foto,
        nome=nome
    )


@app.route("/galeria")
def galeria():

    return render_template("galeria.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)