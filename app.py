from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def portfolio():
    return render_template("index.html")

@app.route("/loading")
def loading():
    return render_template("loading.html")

@app.route("/emi")
def emi():
    return render_template("emi.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json

    total_amount = float(data["total"])
    down_payment = float(data["down"])
    L = total_amount - down_payment

    R = float(data["rate"])
    T = int(data["tenure"])

    M = (R / 100) / 12
    E = (L * M * (1 + M)**T) / ((1 + M)**T - 1)

    return jsonify({"emi": round(E, 2)})

if __name__ == "__main__":
    app.run(debug=True)
