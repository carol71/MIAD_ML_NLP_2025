#!/usr/bin/python
from flask import Flask
from flask_restx import Api, Resource, fields
import joblib
from m09_model_deployment import predict

app = Flask(__name__)

api = Api(
    app, 
    version='1.0', 
    title='Popularity Prediction API',
    description='Popularity Prediction API')

ns = api.namespace('predict', 
     description='Popularity Predictor')
   
parser = api.parser()

parser.add_argument(
    'duration_ms', 
    type=int, 
    required=True, 
    help='Duración en milisegundos', 
    location='args')

parser.add_argument(
    'energy', 
    type=float, 
    required=True, 
    help='Energía de la canción en una escala de 0 a 1', 
    location='args')

resource_fields = api.model('Resource', {
    'result': fields.Float,
})

@ns.route('/')
class PopularityApi(Resource):

    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        duration_ms = args['duration_ms']
        energy = args['energy']
        
        prediction = predict(duration_ms, energy)
        
        return {
         "result": prediction
        }, 200
    
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)
