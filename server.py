from cgitb import html
from flask import Flask, render_template, redirect, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)


# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', 'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(
            f'\n email address: {email}, subject: {subject}, message: {message}')
        # print(file)


# file = pd.read_csv("database.csv")
# headerList = ['email', 'subject', 'message']


def write_to_csv(data):
    with open('database.csv', 'a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
        # print(file)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # print(request.form)
            # print(data)
            file.to_csv("database.csv", header=headerList, index=False)
            write_to_csv(data)
        except:
            return 'An error occured'

        return redirect('thankyou.html')
    else:
        return 'something went wrong'

# @app.route('/components.html')
# def components():
#     return render_template('components.html')


# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')


# @app.route('/index.html')
# def my_home():
#     return render_template('index.html')


# @app.route('/work.html')
# def work():
#     return render_template('work.html')


# @app.route('/works.html')
# def works():
#     return render_template('works.html')


# @app.route('/favicon.ico')
# def favicon():
#     return redirect(url_for('static', filename='favicon_ico.png'), code=302)
