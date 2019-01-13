from flask import Flask
from routes.search import search_blueprint
app = Flask(__name__)
app.register_blueprint(search_blueprint)

if __name__ == "__main__":
    app.run("0.0.0.0",port=8005,debug=False,threaded=True)