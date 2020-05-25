from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    try:
        name="Python"
        example_list = ["2.5, 2.6, 2.7, 2.8"]
        return render_template('index.html', name=name, example_list = example_list) ##Your HTML file
    except Exception as e:
        return str(e)

@app.route('/about/')
def aboutpage():
    name="Python"
    example_list = ["2.5, 2.6, 2.7, 2.8"]
    try:
        return render_template('about.html') ##Your HTML file
    except Exception as e:
        return str(e)

@app.route('/info/')
def infopage():
    try:
        return render_template('info.html') ##Your HTML file
    except Exception as e:
        return str(e)

@app.errorhandler(404)
def four_oh_four(e):
    return render_template("404.html")
    
if __name__ == "__main__":
    app.run()
