from msilib.schema import Class
from flask import render_template

class Calc():

    def home():           
        return render_template('calculator.html')