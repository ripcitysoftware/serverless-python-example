from flask import Flask, jsonify, make_response, abort
from uuid import UUID, uuid4

from flask import request

app = Flask(__name__)

        # Uuid: {S: $uuid},
        # "Name": {"S": "Maki"},
        # "Cloud": {"S": "AWS"},
        # "ProgrammingLanguage": {"S": "Java"},
        # "ProgrammingLanguage2": {"S": "Python"}

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route("/employees", methods=['POST'])
def say_hello():
    if not request.json or not 'Name' in request.json:
        abort(400)
    employee = {
        'id': str(uuid4()),
        'Name': request.json['Name'],
        'Cloud': request.json['Cloud'],
        'ProgrammingLanguage': request.json['pl'],
        'ProgrammingLanguage2': request.json['pl2']
    }
    return jsonify({'Employee': employee}), 201

@app.route("/employees/<uuid:uuid>", methods=['GET'])
def get_employee(uuid):
    print(f'UUID is {uuid}')
    if uuid is None:
        abort(404)

    return jsonify({'employee': str(uuid)})


if __name__ == '__main__':
    app.run(debug=True)


# https://scotch.io/bar-talk/processing-incoming-request-data-in-flask
# https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
#
# curl -X POST -H "Content-Type: application/json" \
#      -d '{"Name": "Chris Lahdesmaki", "Cloud": "AWS", "pl": "Java", "pl2": "Python"}' \
#      -Lik http://127.0.0.1:5000/employees && echo
#
# curl -Lik http://127.0.0.1:5000/employees/$(uuidgen)