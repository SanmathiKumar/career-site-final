from flask import Flask, render_template, jsonify
from database import get_db_jobs 

# Creating the instance of the flask
app = Flask(__name__)

# Registering the route to guide the Flask application
# everthing after "/" is called path or route

# JOBS = [{
#   'id': 1,
#   'title': "Data Analyst",
#   "location": "Bengaluru",
#   "salary": 10000
# }, {
#   'id': 2,
#   'title': "Data Engineer",
#   "location": "Bengaluru",
#   "salary": 8000
# }, {
#   'id': 3,
#   'title': "Data Scientist",
#   "location": "Bengaluru",
#   "salary": 15000
# }, {
#   'id': 4,
#   'title': "Data Expert",
#   "location": "Davangere",
#   "salary": 25000
# }]

# Get the job details from the database
# database.py has the functions which will return the jobs
jobs_list = get_db_jobs()


# Using decorator and defining the path. Here the "/" refers to the homepage
@app.route("/")
def hello():
  return render_template("bootstrap-home.html",
                         jobs=jobs_list,
                         company_name="Aroma")


# Using the API route to display the data via jsonify
# jsonify() will make the objects into JSON format
@app.route("/api/jobs")
def list_jobs():
  return jsonify(jobs_list)


# Since the path of Flask is not defined it is not gonna run, so we need to do some changes.
# The app can be run using the run() function.
# Host should be 0.0.0.0 to run it locally and debug will be true because the new changes will
# reflect immediately.

print(__name__)
if __name__ == "__main__":
  print("Inside main")
  app.run(host="0.0.0.0", debug=True)
