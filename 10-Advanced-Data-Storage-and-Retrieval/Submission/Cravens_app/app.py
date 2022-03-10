import numpy as np
import pandas as pd
from flask import Flask, jsonify
from sqlalchemy import create_engine


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# database setup
path = "sqlite:///Resources/hawaii.sqlite"
engine = create_engine(path)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"""
        <ul>
            <li><a href='/api/v1.0/precipitation'>/api/v1.0/precipitation</a></li><br/>
            <li><a href='/api/v1.0/stations'>/api/v1.0/stations</a></li><br/>
            <li><a href='/api/v1.0/tobs'>/api/v1.0/tobs</a></li><br/>
            <li><a href='/api/v1.0/2012-03-01'>/api/v1.0/2012-03-01'</a></li><br/>
            <li><a href='/api/v1.0/2012-03-01/2012-05-31'>/api/v1.0/2012-03-01/2012-05-31</a></li>
        </ul
        """
    )

@app.route("/api/v1.0/precipitation")
def get_rain():
    conn = engine.connect()
    query = """
        SELECT
            date,
            sum(prcp) as "Total Rain Today"
        FROM
            measurement
        GROUP BY
            date
        ORDER BY
            date;
        """

    df = pd.read_sql(query, conn)
    
    data = df.to_dict(orient="records")
    return(jsonify(data))

@app.route("/api/v1.0/stations")
def get_stations():
    conn = engine.connect()
    query = """
        SELECT
            name,
            station as "Station ID"
        FROM
            station;
        """

    df = pd.read_sql(query, conn)
    
    data = df.to_dict(orient="records")
    return(jsonify(data))


@app.route("/api/v1.0/tobs")
def get_temps():
    conn = engine.connect()
    query = """
        SELECT
            tobs,
            date,
            station
        FROM
            measurement
        WHERE
            date >= '2016-08-23'
            AND station = "USC00519281"
        ORDER BY
            date;
        """

    df = pd.read_sql(query, conn)
    
    data = df.to_dict(orient="records")
    return(jsonify(data))


@app.route("/api/v1.0/<start>")
def get_start_date(start):
    conn = engine.connect()
    query = f"""
        SELECT
            date,
            min(tobs) as tmin,
            max(tobs) as tmax,
            avg(tobs) as tavg
        FROM
            measurement
        WHERE
            date = '{start}'
        """

    df = pd.read_sql(query, conn)
    
    data = df.to_dict(orient="records")
    return(jsonify(data))

@app.route("/api/v1.0/<start>/<end>")
def get_start_end(start, end):
    conn = engine.connect()
    query = f"""
        SELECT
            min(tobs) as tmin,
            max(tobs) as tmax,
            avg(tobs) as tavg
        FROM
            measurement
        WHERE
            date >= '{start}'
            and date <= '{end}'
        """

    df = pd.read_sql(query, conn)
    
    data = df.to_dict(orient="records")
    return(jsonify(data))


if __name__ == '__main__':
    app.run(debug=True)