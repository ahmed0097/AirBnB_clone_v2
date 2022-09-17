#!/usr/bin/python3
"""9-states Module"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_sqlalchemy_sess(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states/', strict_slashes=False)
def list_states():
    """Displays html page"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', my_dict=states)


@app.route('/states/<id>', strict_slashes=False)
def many_states(id):
    """Displays html page"""
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html',
                                   my_state=state, my_cities=state.cities)

    return render_template('9-states.html', found_id=False)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
