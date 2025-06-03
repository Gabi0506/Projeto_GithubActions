from flask import Flask, jsonify # type: ignore
from flask_swagger_ui import get_swaggerui_blueprint # type: ignore
from flask_jwt_extended import JWTManager, create_access_token,jwt_required # type: ignore
import os

#oii

app = Flask(__name__)
# Configuração do JWT
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')


jwt = JWTManager(app)
### Swagger UI ###
SWAGGER_URL = '/swagger'

API_DOC_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL,
API_DOC_URL)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
@app.route('/')

def home():
    return jsonify(message="API is running")
@app.route('/items', methods=['GET'])


def get_items():
    return jsonify(items=["item1", "item2", "item3"])
@app.route('/login', methods=['POST'])

#Teste para workflow GitHub Actions
#Teste para workflow GitHub Actions2


def login():
    access_token = create_access_token(identity="user")
    return jsonify(access_token=access_token)

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify(message="Protected route")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

