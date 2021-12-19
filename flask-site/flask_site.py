import os.path
from flask import Flask, request, flash, redirect
from flask_autoindex import AutoIndex
from flask_simplelogin import SimpleLogin, login_required


UPLOAD_FOLDER = "./uploads"


home_path = str(os.getenv("PWD"))
full_path = os.path.abspath(home_path)


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

app.config["SIMPLELOGIN_USERNAME"] = "123"
app.config["SIMPLELOGIN_PASSWORD"] = "123"

app.config["SIMPLELOGIN_LOGOUT_URL"] = "/logout"
app.config["SIMPLELOGIN_HOME_URL"] = "/"

SimpleLogin(app)
files_index = AutoIndex(app, full_path, add_url_rules=False)


@app.route("/", methods=["POST", "GET"])
@app.route("/<path:path>", methods=["POST", "GET"])
@login_required
def autoindex(path=full_path):
    if request.method == "GET":
        return files_index.render_autoindex(path)
    if request.method == "POST":
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        file = request.files["file"]
        filename = file.filename
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        return files_index.render_autoindex(path)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, threaded=True)

