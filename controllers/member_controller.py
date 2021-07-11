from flask import Flask, Blueprint, blueprints, render_template, request, redirect
import repositories.member_repository as member_repository

from models.member import Member

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    all_members = member_repository.select_all()
    return render_template("/members/index.html", all_members = all_members)

@members_blueprint.route("/members/<id>")
def show(id):
    member = member_repository.select_member(id)
    return render_template("/members/show.html", member = member)

@members_blueprint.route("/members/new")
def new():
    return render_template("/members/new.html")

@members_blueprint.route("/members", methods = ["POST"])
def save():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    member = Member(first_name, last_name)
    member_repository.save_member(member)
    return redirect("/members")