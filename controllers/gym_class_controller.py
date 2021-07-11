from flask import Flask, Blueprint, render_template, request, redirect

import repositories.gym_class_repository as gym_class_repository

from models.gym_class import GymClass

gym_class_blueprint = Blueprint("gym_class", __name__)

@gym_class_blueprint.route("/classes")
def classes():
    all_classes = gym_class_repository.select_all()
    return render_template("/gym_class/index.html", all_classes = all_classes)

