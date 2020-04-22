from flask import jsonify
from flask_restful import Resource

from .runner import run_script


class ScriptRunnerResource(Resource):
    def post(self, script_id=None):
        from endpoints.scripts.model import Script

        script = Script.query.filter_by(id=script_id).first()
        script_path = script.path

        process_output = run_script(script_path)
        return jsonify({
            'output': process_output
        }, 200)