from flask import Flask, render_template, request, redirect, url_for
from data import get_us_cum_deaths

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'
    # return '<h1>Landing Page</h1>'
    # return render_template('index.html')
    # return render_template('index.html', title='Landing Page')


# @app.route('/about')
# def about():
#     # return 'About'
#     return render_template('about.html', title='About')


# @app.route('/home')
# def home():
#     return render_template('home.html')

# userData = [
#     {
#         'username': 'user1',
#         'age': 18,
#         'membership': 'gold'
#     }, 
#     {    
#         'username': 'user2',
#         'age': 19,
#         'membership': 'silver'
#     },
#     {
#         'username': 'user3',
#         'age': 20,
#         'membership': 'bronze'
#     }
# ]

# @app.route('/users')
# def users():
#     return render_template('users.html', userData=userData, title='Users')


# #collect user input
# @app.route('/form', methods=['GET', 'POST'])
# def form():
#     if request.method == 'GET':
#         return render_template('form.html')
#     else: #if POST request
#         first_name = request.form['firstname']
#         last_name = request.form['lastname']
#         return render_template('home.html', title= first_name +' ' + last_name)


# @app.route('/us-cum-deaths', methods=['GET'])
# def us_cum_deaths():
#     return get_us_cum_deaths()