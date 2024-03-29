import random

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

emails_cadastrados = []
@app.route("/")
def principal():
    imagem = [
        "/static/img/gato01.png",
        "/static/img/gato02.png",
        "/static/img/gato03.png",
    ]

    frase = [
        "Os gatos são seres misteriosos que dominam o mundo com sua elegância e graça.",
        "Um ronronar suave é a melodia do contentamento felino, enchendo nossos corações de calor e tranquilidade.",
        "Cada gato é uma obra-prima única da natureza, com sua própria personalidade encantadora e peculiaridades cativantes.",
    ]

    return render_template("index.html",
        imagens=imagem[random.randrange(0,3)],
        frases=frase[random.randrange(0,3)])

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/newsletter", methods=["GET","POST"])
def newsletter():
    if request.method == "GET":
        return render_template("newsletter.html")
    else:
        email = request.form["email"]
        if email == "":
            resultado = "Email invalido"

        else:
            emails_cadastrados.append(email)
            resultado = "Cadastro efetuado com sucesso"
        return render_template("newsletter.html", campo_resultado = resultado)





@app.route("/login", methods=["GET","POST"])
def login():
  if request.method == "GET":
    return render_template("login.html")
  else:
    user = request.form["usuario"].upper()
    senha = request.form["senha"]
    if user != "octavio" and senha != "lindao":
        resultado1 = "email não cadastrado"

    else:
        return redirect("/cadastros")
    return render_template("login.html", campo_resultado2 = resultado1)

@app.route("/cadastros")
def cadastro():
    return render_template("cadastros.html",
                           cadastrados = emails_cadastrados)

#Debug serva para que você não tenha que ficar reiniciando o servidor, basta salvar o arquivo que ele reinicia sozinho
app.run(debug=True)