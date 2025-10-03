from flask import Blueprint, render_template

videos_bp = Blueprint("videos", __name__)

@videos_bp.route("/youtube-to-mp3")
def youtube_to_mp3():
    return render_template("youtubeToMp3.html")

@videos_bp.route("/youtube-to-mp4")
def youtube_to_mp4():
    return render_template("youtubeToMp4.html")