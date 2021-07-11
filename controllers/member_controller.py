from flask import Flask, Blueprint, blueprints, render_template, request, redirect

from models.member import Member

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    return render_template("/members/index.html")

@members_blueprint.route("/members/new")
def new():
    return render_template("/members/new.html")

