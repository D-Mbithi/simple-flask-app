from flask import Flask, render_template, request, url_for, redirect, session

app = Flask(__name__)
app.confing.from_pyfile('settings.py')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello')
def hello_world():
    return 'Hello world!'


@app.route('/hello/<int:planet>')
def hello_planet(planet):
    planet_id = planet
    print(planet_id)
    return render_template('hello.html')


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == "POST":
        first_name = request.values.get('first_name')
        last_name = request.values.get('last_name')
        session['first_name'] = first_name
        return redirect(url_for('registered'))
    return render_template('form.html')


@app.route('/thank_you')
def registered():
    first_name = session.get('first_name')

    return f"Thank you, {first_name}"


if __name__ == "__main__":
    app.debug = True
    app.run()
