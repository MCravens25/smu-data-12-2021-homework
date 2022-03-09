import numpy as np
import pandas as pd
from flask import Flask, jsonify
from sqlHelper import SQLHelper


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# init class
sql = SQLHelper()

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/passengers"
    )

@app.route("/api/v1.0/passengers")
def passengers():

    query = """
        SELECT
            *
        FROM
            passenger;
        """
    data = sql.executeQuery(query)
    return(jsonify(data))

@app.route("/api/v1.0/age/<age>")
def getAge(age):

    query = f"""
        SELECT
            *
        FROM
            passenger
        WHERE
            age <= {age}
        ORDER BY
            age desc;
        """

    data = sql.executeQuery(query)
    return(jsonify(data))

@app.route("/api/v1.0/combo/<age>/<survived>")
def getCombo(age, survived):
    query = f"""
    SELECT
        *
    FROM
        passenger
    WHERE
        age <= {age}
        AND survived = {survived}
    ORDER BY name asc;
    """

    data = sql.executeQuery(query)
    return(jsonify(data))

if __name__ == '__main__':
    app.run(debug=True)
