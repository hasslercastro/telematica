from app import app, bcrypt
from app.schemas.User import User
from app.schemas.Sensor import Sensor
from app.schemas.Allowed import Allowed

from mongoengine import connect, DoesNotExist

from flask import jsonify, request, session
from flask_cors import cross_origin
from datetime import datetime

connect("proyecto0")


@app.route('/push-weather', methods=["POST"])
def push_weather_info():
    """
    Push weather info to the database if the sensor has been registered

    Inside the request post:

        mac_dir -> sensor mac
    """
    if request.method == "POST":

        req = request.get_json()
        points = req.get("points")
        mac_dir = req.get("mac_dir")

        try:
            allowed = Allowed.objects(mac_dir=mac_dir).get()
        except DoesNotExist:
            return jsonify(succes=False, message="Sensor not allowed")

        sensor = Sensor(
            date=datetime.utcnow(),
            weather_data=points
        ).save()

        return jsonify(success=True, message="Points added")

    return jsonify(success=False, message="Bad request")


# get view
@app.route('/get-weather', methods=["GET"])
@cross_origin(supports_credentials=True)
def get_weather_info():
    """
    Returns recorded data, if the user is logged.
    """

    if request.method == "GET":

        username = session.get("USERNAME")

        if username == None:
            return jsonify(succes=False, message="log in first")

        points = []
        for obj in Sensor.objects:
            points.append(obj.weather_data)

        return jsonify(success=True, result=points)

    return jsonify(success=False, message="Bad request")


@app.route("/sign-in", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def sign_in():
    """
    Log-In if the user has been added trought user-register endpoint

    """

    if request.method == "POST":

        req = request.get_json()

        username = req.get("username")
        password = req.get("password")

        try:
            user = User.objects(username=username).get()
        except DoesNotExist:
            return jsonify(success=False, message="User doesn't exist")

        if not bcrypt.check_password_hash(user.password, password):

            return jsonify(success=False, message="Incorrect password")

        session["USERNAME"] = user["username"]

        return jsonify(success=True, message="Logged successfully")

    return jsonify(success=False, message="Bad Request")


@app.route("/sensor-register", methods=["POST"])
def sensor_register():
    """
    Adds a new sensor to the allowed sensors collection
    """

    if request.method == "POST":

        req = request.get_json()

        mac_dir = req.get("mac_dir")

        allowed = Allowed(
            mac_dir=mac_dir
        ).save()

        return jsonify(success=True, message="Sensor has been registered successfully")

    return jsonify(success=False, message="Bad Request")


@app.route("/user-register", methods=["POST"])
def user_register():
    """
    Adds a new user
    """

    if request.method == "POST":

        req = request.get_json()

        username = req.get("username")
        password = req.get("password")

        user = User(
            username=username,
            password=bcrypt.generate_password_hash(password)
        ).save()

        return jsonify(success=True, message="User has been registered successfully")

    return jsonify(success=False, message="Bad Request")
