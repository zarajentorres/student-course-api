"""
Student Course API
Laboratory Activity 3A - System Integration and Architecture

A small, read-only REST API built with Python and Flask.
The course records are stored directly in this file: NO database is used,
and NO create/update/delete operations exist.

Run locally:
    python app.py
Production (Render):
    gunicorn app:app
"""

import os

from flask import Flask, jsonify
from flask_cors import CORS

# The Flask application object. Gunicorn looks for this name in "app:app".
app = Flask(__name__)

# CORS lets a browser page (or another machine) call this API during a
# classroom demonstration. No authentication is required.
CORS(app)

# ---------------------------------------------------------------------------
# Sample data: five fictional university courses.
# Every record has an integer id, a course code, a name, and a short description.
# ---------------------------------------------------------------------------
COURSES = [
    {
        "id": 1,
        "code": "ITAS 3228",
        "name": "Web and Mobile Development",
        "description": "Build responsive websites and mobile-ready interfaces using modern front-end tools and API-driven development.",
    },
    {
        "id": 2,
        "code": "ITAS 3218",
        "name": "Database Management",
        "description": "Design relational schemas, write SQL queries, and keep data accurate through constraints and transactions.",
    },
    {
        "id": 3,
        "code": "ITAS 3208",
        "name": "System Integration and Architecture",
        "description": "Connect separate systems through APIs and integration patterns so enterprise workflows run end to end.",
    },
    {
        "id": 4,
        "code": "ITAS 3238",
        "name": "Computer Networking",
        "description": "Understand network topologies, the TCP/IP model, subnetting, routing, and basic troubleshooting.",
    },
    {
        "id": 5,
        "code": "ITAS 3248",
        "name": "Object-Oriented Programming",
        "description": "Apply classes, objects, inheritance, and polymorphism to write reusable and maintainable software.",
    },
]


# ---------------------------------------------------------------------------
# 1. HEALTH CHECK  ->  GET /api/health
# Tells you the API is running and reachable.
# ---------------------------------------------------------------------------
@app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify({
        "status": "success",
        "message": "Student Course API is running",
    }), 200


# ---------------------------------------------------------------------------
# 2. COURSE LIST  ->  GET /api/courses
# Returns every course as a JSON array.
# ---------------------------------------------------------------------------
@app.route("/api/courses", methods=["GET"])
def get_courses():
    return jsonify(COURSES), 200


# ---------------------------------------------------------------------------
# 3. ONE COURSE  ->  GET /api/courses/<id>
# Returns a single course, or HTTP 404 when the id does not exist.
# ---------------------------------------------------------------------------
@app.route("/api/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    for course in COURSES:
        if course["id"] == course_id:
            return jsonify(course), 200

    return jsonify({
        "status": "error",
        "message": "Course with id {} was not found".format(course_id),
    }), 404


# ---------------------------------------------------------------------------
# Basic error handling: every error still comes back as JSON, never HTML.
# ---------------------------------------------------------------------------
@app.errorhandler(404)
def handle_not_found(error):
    return jsonify({
        "status": "error",
        "message": "The requested resource was not found. Please check the URL.",
    }), 404


@app.errorhandler(405)
def handle_method_not_allowed(error):
    return jsonify({
        "status": "error",
        "message": "This API only accepts GET requests.",
    }), 405


@app.errorhandler(500)
def handle_server_error(error):
    return jsonify({
        "status": "error",
        "message": "An internal server error occurred. Please try again later.",
    }), 500


# ---------------------------------------------------------------------------
# Local development entry point.
# Render provides the PORT variable; 5000 is used when you run it on your PC.
# The host must be 0.0.0.0 so the app is reachable from outside the container.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)