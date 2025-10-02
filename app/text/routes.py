from flask import Blueprint, render_template, request

text_bp = Blueprint("text", __name__)

@text_bp.route("/")
def index():
    return render_template("text.html")

@text_bp.route("/convert", methods=["POST"])
def convert():
    text = request.form.get("text", "")
    mode = request.form.get("mode", "upper")

    if mode == "upper":
        result = text.upper()
    elif mode == "lower":
        result = text.lower()
    elif mode == "capitalize":
        result = text.capitalize()
    else:
        result = text

    return f"Resultado: {result}"