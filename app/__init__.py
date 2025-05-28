from flask import Flask
from flask_cors import CORS
from .database import db
from .routes.post_routes import post_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    # 설정 불러오기
    app.config.from_object('config.Config')

    # DB 초기화
    db.init_app(app)

    # 라우터 등록
    app.register_blueprint(post_bp)

    # 테이블 생성 (개발용)
    with app.app_context():
        db.create_all()

    return app
