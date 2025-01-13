import os
from flask import Flask, jsonify, request
from compare import compare_mfcc

SERVER_PORT = 7777
SERVER_ROOT_DIR = os.path.dirname(__file__)

WEBSITE_STATIC_FOLDER = "website/static/"

ALLOWED_EXTENSIONS = set(["wav", "mp3"])
UPLOAD_FOLDER = "uploads/"
UPLOAD_FILENAME = "sound.wav"
TARGET_FILENAME = "target.wav"

app = Flask(
    __name__,
    static_url_path="",
    static_folder=WEBSITE_STATIC_FOLDER,
)


@app.route("/api")
def api():
    return {"message": "Hello from the API!"}


@app.route("/api/upload-audio", methods=["POST"])
def api_upload_audio():
    if "file" not in request.files:
        return jsonify({"message": "No file part"}), 400

    file = request.files["file"]
    filename = file.filename

    if file.filename == "":
        return jsonify({"message": "No selected file"}), 400

    if not allowedFile(filename):
        return jsonify({"message": "File type not allowed", "filename": filename}), 400

    print("Processing:", filename)
    file.save(os.path.join(SERVER_ROOT_DIR, UPLOAD_FOLDER, UPLOAD_FILENAME))

    message = compare_mfcc(
        UPLOAD_FOLDER + UPLOAD_FILENAME, UPLOAD_FOLDER + TARGET_FILENAME
    )

    return jsonify({"message": message, "filename": filename})


def allowedFile(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


if __name__ == "__main__":
    app.run(port=SERVER_PORT, debug=True)
