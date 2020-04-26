import csv
from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/test')
def test_page():
    return 'Test successful!'


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/#submittedform')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])
