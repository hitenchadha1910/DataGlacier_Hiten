from flask import Flask

app = Flask(__name__) #unique name for flask app

#what requests this can accept

@app.route('/') #http:..www.google.com/
def home():
    return "Hello World"

app.run(port=5000)