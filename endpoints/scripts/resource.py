from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from .model import Script
from app import db

script_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'path': fields.String
}

script_post_parser = reqparse.RequestParser()
script_post_parser.add_argument('name', type=str, required=True, location=['json'],
                              help='name parameter is required')
script_post_parser.add_argument('description', type=str, required=True, location=['json'],
                              help='description parameter is required')
script_post_parser.add_argument('path', type=str, required=True, location=['json'],
                              help='path parameter is required')


class ScriptResource(Resource):
    def get(self, script_id=None):
        if script_id:
            script = Script.query.filter_by(id=script_id).first()
            return marshal(script, script_fields)
        else:
            args = request.args.to_dict()
            limit = args.get('limit', 0)
            offset = args.get('offset', 0)

            args.pop('limit', None)
            args.pop('offset', None)

            scripts = Script.query.filter_by(**args).order_by(Script.id)
            if limit:
                scripts = scripts.limit(limit)

            if offset:
                scripts = scripts.offset(offset)

            scripts = scripts.all()

            return marshal(scripts, script_fields)

    @marshal_with(script_fields)
    def post(self):
        args = script_post_parser.parse_args()

        script = Script(**args)
        db.session.add(script)
        db.session.commit()

        return script

    @marshal_with(script_fields)
    def put(self, script_id=None):
        script = Script.query.get(script_id)

        if 'name' in request.json:
            script.name = request.json['name']

        if 'description' in request.json:
            script.description = request.json['description']

        if 'path' in request.json:
            script.path = request.json['path']

        db.session.commit()
        return script

    @marshal_with(script_fields)
    def delete(self, script_id=None):
        script = Script.query.get(script_id)

        db.session.delete(script)
        db.session.commit()

        return script