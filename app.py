from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory storage for courses
courses = []
next_id = 1


# Endpoint to add a course
@app.route('/courses', methods=['POST'])
def add_course():
    global next_id
    data = request.json
    if not data or 'title' not in data or 'description' not in data or 'duration' not in data:
        abort(400)  # Bad request
    course = {
        'id': next_id,
        'title': data['title'],
        'description': data['description'],
        'duration': data['duration']
    }
    courses.append(course)
    next_id += 1
    return jsonify(course), 201


# Endpoint to retrieve all courses
@app.route('/courses', methods=['GET'])
def get_courses():
    return jsonify(courses)


# Endpoint to update a course by ID
@app.route('/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    data = request.json
    course = next((c for c in courses if c['id'] == course_id), None)
    if course is None:
        abort(404)  # Course not found
    if 'title' in data:
        course['title'] = data['title']
    if 'description' in data:
        course['description'] = data['description']
    if 'duration' in data:
        course['duration'] = data['duration']
    return jsonify(course)


# Endpoint to delete a course by ID
@app.route('/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    global courses
    courses = [c for c in courses if c['id'] != course_id]
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)
