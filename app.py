from flask import Flask, render_template, redirect, url_for, request

import passenger
import users
from passenger import Passenger
from flight import Flight, find_vehicle

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
        passenger_new = Passenger(request.form["fname"],
                                  request.form["lname"],
                                  request.form["passport"],
                                  request.form["age"])
        passenger_new.add_record()
        return redirect(url_for("homepage"))
    return render_template('creatingpassenger.html')


@app.route("/passengerrecords")
def passenger_record():
    record = passenger.get_passenger()
    html_start = """ 
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <title>Passenger Records</title>
      <style>

    body{

    }
    html{
    background-image: url("img_12.png") !important;
    }

    .intro
    {
    top:20%;
    }

    table td,
    table th {
      text-overflow: ellipsis;
      white-space: nowrap;
      overflow: hidden;

    }

    thead th {
      color: #fff;
    }

    .card {
      border-radius: .5rem;
    }

    .table-scroll {
      border-radius: .5rem;
    }

    .table-scroll table thead th {
      font-size: 1.25rem;
    }
      </style>
    </head>
    <body><section class="intro">
      <div class="bg-image h-100" style="background-image: url(img_12.png);">
        <div class="mask d-flex align-items-center h-100">
          <div class="container">
            <div class="row justify-content-center">
              <div class="col-12">
                <div class="card">
                  <div class="card-body p-0">
                    <div class="table-responsive table-scroll" data-mdb-perfect-scrollbar="true" style="position: relative; height: 700px">"""
    start_tag = '<table class="table table-striped mb-0">' \
                '<thead style="background-color: #002d72;"><tr><th scope="col">' \
                'First Name</th><th scope="col">Last Name</th><th scope="col">Age</th>' \
                '<th scope="col">Passport ID</th>' \
                '</tr></thead><tbody>'
    start_tag = html_start + start_tag
    string = ""
    for passenger_list in record:
        temp = f"<tr>" \
               f"<td>{passenger_list[0]}</td>" \
               f"<td>{passenger_list[1]}</td>" \
               f"<td>{passenger_list[3]}</td>" \
               f"<td>{passenger_list[2]}</td>" \
               f"</tr>"
        string += temp
    start_tag += string
    start_tag += "</tbody></table>"
    return start_tag


@app.route("/create_flight", methods=["GET", "POST"])
def create_flight():
    if request.method == "POST":
        vehicle = find_vehicle(request.form["vehicleID"])
        if vehicle is not None:
            flight = Flight(request.form["flight_id"],
                            request.form["destination"],
                            request.form["origin"],
                            request.form["vehicleID"],
                            request.form["duration"])
            flight.add_records()
    else:
        render_template("createflight.html")


if __name__ == "__main__":
    app.run(debug=True)
