#!/opt/docker/flask/venv/bin/python3
from flask_site import app
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, threaded=True)