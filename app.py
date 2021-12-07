import numpy as np
from flask import Flask, request, jsonify, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os
import pickle
import pdfplumber
import re
from magic import maya,checkforme
import html

ALLOWED_EXTENSIONS = {'pdf'}
prediction_text = {}

app = Flask(__name__)

@app.route('/')

def home():

    return render_template('home.html')


@app.route("/result", methods = ['GET','POST'])

def predict():    
    if request.method == 'POST':
        cps = request.files['file']
        
        wyn = maya(cps)

        prediction_text = wyn
        check_list = checkforme(wyn)

        cps27 = html.unescape(check_list['cps27'])
        cps01 = html.unescape(check_list['cps01'])
        cps05 = html.unescape(check_list['cps05'])

        return render_template('result.html', prediction_text = prediction_text, check_list = check_list, cps27 = cps27, cps01=cps01, cps05=cps05) 

if __name__ == '__main__':
    app.run(debug=True)
