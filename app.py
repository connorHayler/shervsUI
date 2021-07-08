from flask import Flask, render_template, redirect, url_for, request

import passenger
import users
from passenger import Passenger, get_passenger
from flask_table import Table, Col

app = Flask(__name__)


@app.route("/sign_up", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if users.login(request.form["username"], request.form["password"]) is False:
            error = "That username and passport combination does not match"
        else:
            return redirect(url_for("homepage"))
    return render_template('sign_up.html', error=error)


@app.route("/homepage")
def homepage():
    return render_template("homepage.html")


@app.route("/createpassenger", methods=["GET", "POST"])
def create_passenger():
    if request.method == "POST":
        passenger = Passenger(request.form["fname"],
                              request.form["lname"],
                              request.form["passport"],
                               request.form["age"])
        passenger.add_record()
        return redirect(url_for("homepage"))
    return render_template('creatingpassenger.html')

@app.route("/passengerrecords")
def passenger_record():
    record = Passenger.get_passenger()
    tag = "<tbody>"
    string = ""
    for passenger in record:
        temp = f"<tr>"\
               f"<td></td>"\
               f"</tr>"







if __name__ == "__main__":
    app.run(debug=True)
