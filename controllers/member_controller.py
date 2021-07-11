from flask import Flask, Blueprint, render_template, request, redirect

from models.member import Member

member_blueprint = Blueprint("member", __name__)