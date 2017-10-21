from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Portfolio.html')

@app.route('/projects')
def webpage():
    return render_template('MyWebPage.html')

@app.route('/about')
def aboutme():
    return render_template('AboutMe.html')


app.run(debug=True)