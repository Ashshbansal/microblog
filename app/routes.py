from app import app
from flask import render_template
#decorators
@app.route('/')   
@app.route('/index')
# view function
def index(): 
    user={"username":"Ashish"}
    posts=[
        {
            'author' : {'username' : 'Aman'},
            'body': "Let's Play tennis today"
            
        },
        {
            'author' : {'username' : 'Ashish'},
            'body': "Sure will play tennis"
        }
    ]

    return render_template('index.html',title="Home page",user=user,posts=posts)
    