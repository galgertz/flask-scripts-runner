from flask import Flask, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import default_exceptions
import settings
from endpoints.scripts_runner.resource import ScriptRunnerResource

app = Flask(__name__)


@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code


for ex in default_exceptions:
    app.register_error_handler(ex, handle_error)

app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['BUNDLE_ERRORS'] = settings.BUNDLE_ERRORS

db = SQLAlchemy(app)
api = Api(app)
api.prefix = '/api'

from endpoints.scripts.resource import ScriptResource

# api.add_resource(UsersResource, '/users', '/users/<int:user_id>')
api.add_resource(ScriptResource, '/scripts', '/scripts/<int:script_id>')
api.add_resource(ScriptRunnerResource, '/script_run/<int:script_id>')

if __name__ == '__main__':
    app.run(debug=True)
