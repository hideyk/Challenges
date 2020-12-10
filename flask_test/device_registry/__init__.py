import os
from flask import Flask
from flask_restful import Api, Resource
import markdown


# Create an instance of Flask
app = Flask(__name__)
api = Api(app)
# @app.route("/users")
# def index():
#     """Present some documentation"""
#
#     Open the README file
    # with open(os.path.dirname(app.root_path) + "/README.md", "r") as markdown_file:
    #     content = markdown_file.read()
    #     return markdown.markdown(content)

class Users(Resource):
    def get(self):
        with open(os.path.dirname(app.root_path) + "/README.md", "r") as markdown_file:
            content = markdown_file.read()
            return markdown.markdown(content), 200

api.add_resource(Users, "/users")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080', debug=True)