from flask import Flask,render_template

#Create a Flask Instance 
app = Flask(__name__)

#Create route decorator
@app.route('/')
# def index():
#     return '<h1>Hello world!.</h1>'

# safe -> to String of html into actual html code
# upper
# lower 
# title -> capitalize all the first letter
# trim 
# capitalize 
# striptags -> remove any html tag present in the string 
# 

def index():
    first_name = 'hari'
    stuff = 'this is <strong> Bold </strong> character'
    animal_list = ['Dog','Cat','lion' , 21012 ]
    return render_template('index.html' , first_name = first_name ,
                           stuff = stuff,animal_list = animal_list)


#http://localhost:5000/user/Hari
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name = name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"),500

