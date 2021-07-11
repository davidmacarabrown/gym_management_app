from flask import Flask, Blueprint, render_template, request, redirect

from models.gym_class import GymClass

gym_class_blueprint = Blueprint("gym_class", __name__)

