from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    foto = None
    nome = None
    mensagem = None

    fotos = {
        "gustavo": "gustavo.jpg",
        "richard": "richard.jpg",
        "matheus": "matheus.jpg",
        "miguel": "miguel.jpg",
        "jose": "jose.png",
        "flavio": "flavio.jpg",
        "kayo": "kayo.jpg",
        "kaique": "kaique.jpg"
    }

    if request.method == "POST":

        nome = request.form["nome"]

        nome_formatado = nome.strip().lower()

        if nome_formatado in fotos:
            foto = fotos[nome_formatado]
        else:
            mensagem = "Esse cabrito ainda não foi cadastrado 😂"

    return render_template(
        "index.html",
        foto=foto,
        nome=nome,
        mensagem=mensagem
    )


@app.route("/galeria")
def galeria():

    return render_template("galeria.html")


if __name__ == "__main__":
    app.run(debug=True)