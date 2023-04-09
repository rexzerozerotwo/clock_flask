# make a script where when u upload a image it copy to "important" path and also delete the uploaded copy
from flask import Flask, url_for, render_template, request
from datetime import date, datetime
import pytz

application = Flask(__name__)
app = application
def return_time_obj():
    time_obj = []
    today_time = date.today()
    curr_local_now = datetime.now().strftime("%H:%M:%S")
    curr_ny_time = datetime.now(pytz.timezone('US/Eastern')).strftime("%d:%m:%y Day %H:%M:%S Hrs")
    time_obj.append(today_time)
    time_obj.append(curr_local_now)
    time_obj.append(curr_ny_time)
    return time_obj

@app.route('/')
def form():
    date_time = return_time_obj()
    timezone_List = [
        'America/New_York',
        'US/Eastern',
        'America/Los_Angeles',
        'Europe/London',
        'Europe/Paris',
        'Asia/Kolkata',
        'Asia/Shanghai',
        'Asia/Tokyo',
        'Asia/Seoul'
        ]
    return render_template('input.html', timezone_List=timezone_List, today=date_time[0], lc_now=date_time[1], ny_now=date_time[2])

@app.route('/',methods=["POST"])
def get_time():
    if request.method == "POST":
        dateTime = request.form['dateTime']
        timezone = request.form['timezone']
        input_time = datetime.strptime(dateTime.replace('T',' '), '%Y-%m-%d %H:%M')
        output_time = input_time.astimezone(pytz.timezone(timezone))
    return render_template('input.html', submitted=True, timezone=timezone, input_time=input_time, output_time=output_time)


# @app.route('/')
# def index():
#     return 'index'

# @app.route('/login')
# def login():
#     return 'login'

# @app.route('/user/<username>')
# def profile(username):
#     return f'{username}\'s profile'

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))

# @app.route("/")
# def hello_world():
#     return '''
# <p>Hello, World!</p>
# '''

# @app.route("/kenobi")
# def hello_there ():
#     return '''
#     <h1>hello there!</h1>
# '''

# @app.route("/shash/")
# def without_shash():
#     return '''
#     <h1>ok</h1>
# '''

# @app.route("/shash")
# def withshash():
#     return '''
#     <h1>OK!</h1>
# '''
