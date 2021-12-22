from flask import Flask, render_template

app=Flask(__name__)


@app.route('/')
@app.route('/index')

def home():
    posts = ['post1','post2','post3','post4','post5']
    return render_template('index.html', posts=posts ) #passing the posts to the html 

if __name__ == '__main__':
    app.run(debug=True)