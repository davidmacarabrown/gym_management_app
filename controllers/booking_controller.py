from flask import Flask, Blueprint, render_template, request, redirect

from models.booking import Booking

import repositories.booking_repository as booking_repository

bookings_blueprint = Blueprint("booking", __name__)

@bookings_blueprint.route("/bookings/new")
def create_booking():
    return render_template("/bookings/new.html")
    
    

