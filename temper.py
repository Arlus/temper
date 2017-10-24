from __future__ import division
from werkzeug.contrib.fixers import ProxyFix
from collections import OrderedDict
from flask import Flask, render_template
import csv
import os

app = Flask(__name__)

onboarding_steps = [0, 20, 40, 50, 70, 90, 99, 100]


def import_data(file_path):
    with open(file_path, "rb") as csvfile:
        datareader = csv.reader(csvfile)
        next(datareader)
        for row in datareader:
            yield row


def format_data(filename):
    step_counts = OrderedDict()
    step_counts[0], step_counts[20], step_counts[40], step_counts[50], step_counts[70], step_counts[90], step_counts[99], step_counts[100] = 0, 0, 0, 0, 0, 0, 0, 0
    users_count = 0
    for row in import_data(filename):
        if int(float(row[2])) not in onboarding_steps:
            break
        users_count += 1
        key = int(float(row[2]))
        step_counts[key] += 1
        for step in onboarding_steps:
            if step < key:
                step_counts[step] = step_counts[step] + 1
    step_percentages = [int(value / users_count * 100) for key, value in step_counts.items()]
    return step_percentages


@app.route('/')
def chart():
    file_path = os.path.join(app.root_path, 'export.csv')
    data = format_data(file_path)
    return render_template("index.html", data=data, steps=onboarding_steps)


app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.run()
