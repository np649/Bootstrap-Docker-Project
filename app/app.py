"""A simple flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from werkzeug.debug import DebuggedApplication
from flask import render_template

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()

@app.route("/TheBeginning", methods=["GET"])
def test_get1():
    return render_template('The_Beginning.html')

@app.route("/BrowserWars", methods=["GET"])
def test_get2():
    return render_template('Browser_Wars.html')

@app.route("/Concepts", methods=["GET"])
def test_get3():
    return render_template('Concepts_and_Glossary.html')

@app.route("/OOP", methods=["GET"])
def test_get4():
    return render_template('OOP.html')
