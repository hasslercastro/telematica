from app import app, bcrypt

from mongoengine import connect, DoesNotExist

from app.schemas.User import User

from flask import jsonify, request, session

from flask_cors import cross_origin

connect("proyecto0")


@app.route('/push-weather', methods=["POST"])
def push_weather_info():
    
    if request.method == "POST":

        req = request.get_json()

        username = req.get("username")
        points = req.get("points")

        try:
            user = User.objects(username=username).get()
        except DoesNotExist:
            return jsonify(success=False, message="User doesn't exist")

        for point in points:
            user.weather_data.append(point)
        
        user.save()

        return jsonify(success=True, message="Points added")

    return jsonify(success=False, message="Bad request")


#get view
@app.route('/get-weather', methods = ["POST", "GET"])
@cross_origin(supports_credentials=True)
def get_weather_info():

    if request.method == "POST":

        req = request.get_json()

        username = req.get("username")

        try:
            user = User.objects(username=username).get()
        except DoesNotExist:
            return jsonify(success=False, message="User doesn't exist")
        
        return jsonify(success=True, result=user.weather_data)
    

    else:

        username = session["USERNAME"]

        if username == None:
            return jsonify(succes=False, message="log in first")

        try:
            user = User.objects(username=username).get()
        except DoesNotExist:
            return jsonify(success=False, message="User doesn't exist")
        
        return jsonify(success=True, result=user.weather_data)
    

    
    return jsonify(success=False, message="Bad request")



@app.route("/sign-in", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def sign_in():

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
        
        print(session)

        return jsonify(success=True, message="Logged successfully")
    
    
    return jsonify(success=False, message="Bad Request")    


@app.route("/register", methods=["POST"])
def register():

    if request.method == "POST":
        
        req = request.get_json()

        username = req.get("username")
        password = req.get("password")

        user = User(
            username = username,
            password = bcrypt.generate_password_hash(password), 
            weather_data = [],
        ).save()

        return jsonify(success=True, message="Register successfully")
    
    
    return jsonify(success=False, message="Bad Request")    
