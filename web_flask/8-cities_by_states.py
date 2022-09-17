#!/usr/bin/python3
"""8-cities_by_states Module"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Displays html page"""
    states = storage.all(State).values()
    my_cities = list()

    for state in states:
        for city in state.cities:
            my_cities.append(city)

    return render_template('8-cities_by_states.html',
                           my_state=states, my_cities=my_cities)


@app.teardown_appcontext
def close_sqlalchemy_sess(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0")
