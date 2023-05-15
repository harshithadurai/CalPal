import os
from flask import Flask, redirect, send_file, render_template, request, url_for
import openai
import copy
from create_ical import create_ical

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        info = request.form["info"]

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt1(info),
            temperature=0,
            max_tokens=200,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

        data = response.choices[0].text
        rows = create_rows(data)

        rows_copy = copy.deepcopy(rows)
        rows_ical = create_rows_ical(rows_copy)

        create_ical(rows_ical) 

        return render_template("index.html", rows=rows, rows_ical=rows_ical)

    rows = request.args.get("rows")
    rows_ical = request.args.get("rows_ical")
    return render_template("index.html", rows=rows, rows_ical=rows_ical)


def create_rows(data):
    # Split the string into individual rows
    rows_temp = data.split("\n")
    rows_temp.pop(0)

    # Initialize the list of rows lists
    rows = []

    # Iterate over each row and split it into columns
    for row in rows_temp:
        # Remove leading and trailing spaces
        row = row.strip()

        # Split the row into columns based on the delimiter "|"
        rows.append([col.strip() for col in row.split("|")])

    return rows

def create_rows_ical(rows):

    rows_ical = []
    dates = []
    
    for row in rows:
        dates.append(row[1])

    response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt2(dates),
            temperature=0,
            max_tokens=200,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

    data = response.choices[0].text

    dates = []

    # Split the string into individual rows
    rows_temp = data.split("\n")
    rows_temp.pop(0)

    # Iterate over each row and split it into columns
    for row in rows_temp:
        # Remove leading and trailing spaces
        row = row.strip()

        # Split the row into columns based on the delimiter "|"
        dates.append(row.split("|")[1])

    i = 0
    for row in rows:
        row[1] = dates[i]
        rows_ical.append(row)
        i += 1

    return rows_ical


def generate_prompt1(info):
    return """A 3 column table summarizing this: 

{}

Event Name | Time, Date | Additional Info""".format(info)

def generate_prompt2(dates):
    dates_string = "\n"
    for date in dates:
        dates_string += date + '\n'
    return """Convert this to this format: YYYY MM DD T HH MM SS and create 2-column table. Use X for invalid formats. Assume the year is 2023 if not provided.
{}
Original | Converted""".format(dates_string)

@app.route('/download')
def download():
    path = 'this.ics'
    return send_file(path, as_attachment=True)