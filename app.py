from flask import Flask, jsonify, make_response, abort

from employee import Employee

employee = Employee()

from flask import request

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route("/employees", methods=['POST'])
def create_employee():
    if not request.json or not 'name' in request.json:
        abort(400)

    response = employee.save_employee(request)

    return jsonify({'Employee': response}), 201

@app.route("/employees/<uuid:uuid>", methods=['GET'])
def get_employee(uuid):
    print(f'UUID is {uuid}')
    if uuid is None:
        abort(404)

    response = employee.get_employee(uuid)

    return jsonify({'employee': response})


if __name__ == '__main__':
    app.run(debug=True)
