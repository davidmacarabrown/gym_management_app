from flask import Flask, Blueprint, render_template, request, redirect

from app import app

@app.route("/")
def index():
    return render_template("index.html")