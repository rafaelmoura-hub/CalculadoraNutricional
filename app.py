from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calcular", methods=["POST"])
def calcular():
    peso = float(request.form["peso"])
    objetivo = request.form["objetivo"]

    if objetivo == "ganho":
        proteina = peso * 2.2
        carboidrato = peso * 5
    else:
        proteina = peso * 2.0
        carboidrato = peso * 2.5

    return render_template(
        "resultado.html",
        peso=peso,
        objetivo=objetivo,
        proteina=round(proteina, 1),
        carboidrato=round(carboidrato, 1)
    )


if __name__ == "__main__":
    app.run(debug=True)