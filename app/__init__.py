from flask import Flask
from flask import render_template

def create_app():
    app = Flask(__name__)

    from app.videos import videos_bp
    from app.text import text_bp

    app.register_blueprint(videos_bp, url_prefix="/videos")
    app.register_blueprint(text_bp, url_prefix="/text")

    @app.route("/")
    def homepage():
        return render_template("homePage.html")

    return app