from flask import Flask, Blueprint, render_template, request, redirect
import pdb
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
    member_id = request.form["member_id"]
    class_id = request.form["class_id"]
    member = member_repository.select_member(member_id)
    gym_class = gym_class_repository.select_class(class_id)
    booking_result = booking_repository.save_booking(member, gym_class)

    if booking_result:
        return redirect("/")

    else:
        return redirect("/bookings/error")

@bookings_blueprint.route("/bookings/<class_id>", methods = ["POST"])
def delete_booking(class_id):

    class_id = int(class_id)
    member_id = int(request.form["member_id"])
    booking_to_remove = booking_repository.select_booking_by_class_and_member_id(class_id, member_id)
    booking_repository.delete_booking(booking_to_remove)
    return redirect("/classes")
    
@bookings_blueprint.route("/bookings/error")
def booking_error():
    return render_template("/bookings/error.html")