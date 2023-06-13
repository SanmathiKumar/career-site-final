from flask import Flask

# Creating the instance of the flask
app = Flask(__name__)

# Registering the route to guide the Flask application
# everthing after "/" is called path or route


# Using decorator and defining the path. Here the "/" refers to the homepage
@app.route("/")
def hello():
  return "Hello, Sam!"


# Since the path of Flask is not defined it is not gonna run, so we need to do some changes.
# The app can be run using the run() function.
# Host should be 0.0.0.0 to run it locally and debug will be true because the new changes will
# reflect immediately.

print(__name__)
if __name__ == "__main__":
  print("Inside main")
  app.run(host="0.0.0.0", debug=True)
