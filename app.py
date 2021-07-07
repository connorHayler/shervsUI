from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route("/sign_up", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form["username"] != "admin" or request.form["password"] != "admin":
            error = "That username and passport combination does not match"
        else:
            return redirect(url_for("homepage"))
    return render_template('sign_up.html', error=error)


@app.route("/homepage")
def homepage():
    return render_template("homePage.html")


if __name__ == "__main__":
    app.run(debug=True)
