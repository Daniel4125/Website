from flask import Flask, render_template, Blueprint

app = Flask(__name__)

#profile = Blueprint('home', __name__, )


@app.route('/')
def hello() -> 'html':
    return render_template('home/index.html')

@app.route('/hello')
def helloworld() -> 'html':
    return render_template('hello.html')

@app.route('/autonomouse_agents')
def autonomouse_agents() -> 'html':
    return render_template('autonomouse_agents.html')

@app.route('/cellular_automata')
def cellular_automata() -> 'html':
    return render_template('cellular_automata.html')

@app.route('/fractals')
def fractals() -> 'html':
    return render_template('fractals.html')

@app.route('/evolution')
def evolutionary_algorithms() -> 'html':
    return render_template('evolution.html')

@app.route('/neural-networks')
def neural_networks() -> 'html':
    return render_template('neural-networks.html')



#"Dunder name dunder main"
#True when ran directly by python (py -3)
#False when imported. This ignores app.run() line of code when
#PythonAnywhere imports the script.
if __name__ == '__main__':
    app.run(debug=True)