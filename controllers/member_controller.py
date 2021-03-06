from flask import Flask, Blueprint, blueprints, render_template, request, redirect
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository

from models.member import Member

import pdb

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

@members_blueprint.route("/members/<id>/edit")
def edit(id):
    member = member_repository.select_member(id)
    return render_template("/members/edit.html", member = member)

@members_blueprint.route("/members/<id>", methods = ["POST"])
def save_edit(id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    member = Member(first_name, last_name, id)
    member_repository.update_member(member)
    return redirect("/members")


@members_blueprint.route("/members/<id>/delete")
def delete_member(id):
    id_to_remove = int(id)
    member_repository.delete_member(id_to_remove)
    print(member_repository.select_all())
    # pdb.set_trace()
    return redirect("/members")
    

