#!/usr/bin/env python3
from flask import Blueprint, render_template


oefen = Blueprint('oefen', __name__)


@oefen.route('/')
def index():
    return render_template('home/index.html')


