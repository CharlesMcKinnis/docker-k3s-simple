#!/usr/bin/env python3

# https://www.section.io/engineering-education/deploy-docker-container-to-kubernetes-cluster/
from flask import Flask, render_template
import flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)