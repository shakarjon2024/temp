from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def temp():
    msg = ""

    if request.method == "POST":
        t = float(request.form.get("temp"))

        if t > 37:
            msg = "Kasalsiz 🤒"
        else:
            msg = "Sog‘lom 👍"

    return render_template("temp.html", msg=msg)

if __name__ == "__main__":
    app.run(debug=True)
