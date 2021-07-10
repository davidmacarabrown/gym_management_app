from flask import Flask, Blueprint, render_template, request, redirect

from models.booking import Booking
import repositories.booking_repository as booking_repository

booking_blueprint = Blueprint("booking", __name__)