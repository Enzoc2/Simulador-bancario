from flask import Blueprint, render_template, redirect, url_for
from website.database import execute_sql

routes = Blueprint('routes', __name__)  

@routes.route('/')
def home():
    return render_template('home.html')