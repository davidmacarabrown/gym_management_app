from flask import Flask, Blueprint, render_template, request, redirect

from models.booking import Booking

import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository

bookings_blueprint = Blueprint("booking", __name__)

@bookings_blueprint.route("/bookings/new")
def create_booking():
    all_members = member_repository.select_all()
    all_classes = gym_class_repository.select_all()
    return render_template("/bookings/new.html", all_members = all_members, all_classes = all_classes)

@bookings_blueprint.route("/bookings", methods = ["POST"])
def save_booking():
    member = member_repository.select_member(request.form["member_id"])
    gym_class = gym_class_repository.select_class(request.form["class_id"])
    booking_repository.save_booking(member, gym_class)
    return redirect("/")