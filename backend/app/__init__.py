from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from app.config import config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
bcrypt = Bcrypt()


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)

    # Handle CORS manually
    @app.before_request
    def handle_options():
        if request.method == 'OPTIONS':
            response = Response()
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
            response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
            return response

    @app.after_request
    def add_cors_headers(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
        return response

    @app.errorhandler(Exception)
    def handle_exception(e):
        response = jsonify({'error': str(e)})
        response.status_code = 500
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        return response

    # Register blueprints
    from app.routes.auth import auth_bp
    from app.routes.user import user_bp
    from app.routes.face_detection import face_detection_bp
    from app.routes.chat import chat_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(user_bp, url_prefix='/api/user')
    app.register_blueprint(face_detection_bp, url_prefix='/api/detection')
    app.register_blueprint(chat_bp, url_prefix='/api/chat')

    # Health check
    @app.route('/api/health')
    def health_check():
        return {'status': 'healthy', 'message': 'AI Demo API is running'}

    return app