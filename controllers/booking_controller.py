from flask import Flask, Blueprint, render_template, request, redirect

from models.booking import Booking

booking_blueprint = Blueprint("booking", __name__)
