#!/usr/bin/python3
"""
Script that starts a Flask web application:
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Display a HTML page like in 6-index.html."""
    states = sorted(storage.all("State").values(), key=lambda x: x.name)
    amenities = sorted(storage.all("Amenity").values(), key=lambda x: x.name)

    for state in states:
        state.cities = sorted(state.cities, key=lambda x: x.name)
    
    return render_template(
        "10-hbnb_filters.html",
        states=states,
        amenities=amenities,
    )



@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
