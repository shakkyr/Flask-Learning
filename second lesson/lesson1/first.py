import re
from flask import Flask, request , redirect ,url_for

app = Flask(__name__)

@app.route('/')
def home():
    return 'Home Page'


# @app.route('/about')
# def about():
#     return 'About Page'


# @app.route('/user/<username>')
# def show_user(username):
#     return 'User {}'.format(username)




# @app.route('/post/<int:post_id>')
# def show_posts(post_id):
#     return 'Post {}'.format(post_id)


# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     return 'Subpath {}'.format(subpath)

# # http://127.0.0.1:5000/members?first_name=shadi%20rada&last_name=rada
# @app.route('/members')
# def show_user_profile():
#     first_name = request.args.get('first_name')
#     last_name = request.args.get('last_name')
#     return '<h3>First Name: {} <br>Last Name: {} </h3>'.format(first_name, last_name)


@app.route('/admin')
def hello_admin():
    return 'Hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello {} as Guest'.format(guest)


@app.route('/user/<name>')
def hello_user(post_id):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest = name))



@app.route('/shadi', methods = ['POST', 'GET'])
def shadi():
    if request.method == 'POST':
        return 'you are using POST method'
    else:
        return 'you are using GET method'


if __name__ == '__main__':
    app.run()  
    # app.run(port=5000) # to change port
    # app.run(debug=True)  #activate debug mode
