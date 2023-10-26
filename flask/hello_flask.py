# hello_flask.py
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

# create an instance of Flask
app = Flask(__name__)

boostrap = Bootstrap5(app)

# route decorator binds a function to a URL
@app.route('/')
def hello():
   return '<p>Hello world from Flask! SNAFU - status normal all fouled up. But to really mess things up you need a computer. </p>'

@app.route('/Colin')
def t_test():
    return render_template('template.html')
