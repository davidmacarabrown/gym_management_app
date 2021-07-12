from flask import Flask, Blueprint, render_template, request, redirect

from models.booking import Booking

bookings_blueprint = Blueprint("booking", __name__)

@bookings_blueprint.route("/bookings")
def bookings():
    return render_template("/bookings/index.html")
