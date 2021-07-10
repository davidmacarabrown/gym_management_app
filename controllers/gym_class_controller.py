from flask import Flask, Blueprint, render_template, request, redirect

from models.gym_class import Gym_Class

import repositories.gym_class_repository as gym_class_repository

gym_class_blueprint = Blueprint("gym_class", __name__)

