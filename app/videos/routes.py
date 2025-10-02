from flask import Blueprint, render_template

videos_bp = Blueprint("videos", __name__)

@videos_bp.route("/")
def index():
    return render_template("videos.html")