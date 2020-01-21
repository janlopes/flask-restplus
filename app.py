from flask import Flask
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app)

task_model = api.model('Task', { 'task': fields.String('Infor a pending task.')} )

tasks = []
garbage_out = {'task':'Take the garbage collector out.'}
tasks.append(garbage_out)

@api.route('/tasks')
class task(Resource):

    def get(self):
        return tasks

    @api.expect(task_model)
    def post(self):
        tasks.append(api.payload)
        return {'result': 'Task added'}, 200

if __name__ == '__main__':
 app.run(debug=True)