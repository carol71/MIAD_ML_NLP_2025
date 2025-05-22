from flask import Flask
from flask_restx import Api, Resource, fields
import joblib
from  model_deployment.m09_model_deployment import predict_genres


app = Flask(__name__)
api = Api(app, version='1.0', title='Clasificación de géneros de películas', description='Predicción del género de una película dado la sinopsis.')

ns = api.namespace('predict', description='Clasificación de género')

parser = api.parser()

parser.add_argument('plot', type=str, required=True, help='Agrega la sinopsis de la película', location='args')

resource_fields = api.model('Resource', {
    'genres': fields.List(fields.String),
})

@ns.route('/')
class GenreApi(Resource):
    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        plot = args['plot']
        genres = predict_genres(plot)
        return {"genres": genres}, 200

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)