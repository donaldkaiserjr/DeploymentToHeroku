from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "THIS IS WORKING!"


if __name__ == '__main__':
    app.run()


#create a virtual environment
# conda create -n flaskdeploy flask
#pip install gunicorn
#pip freeze > requirements.txt
# create a new file (right click on DEPLOYMENT_EXAMPLE folder and then crete Procfile.py)
# Inside the Procfile, type in:  web: gunicorn app:app
# Download the Heroku installer (install the Git if you haven't)
# Setup free account on Heroku
# Create a new app
# In command line type:   heroku login
# next, type:  git init
# heroku git:remote -a donald-website
# git add . 
# git commit -am "new commit"
# git push heroku master