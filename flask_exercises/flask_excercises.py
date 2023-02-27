from flask import Flask, request

app = Flask(__name__)
users = {}


class FlaskExercise:
    @staticmethod
    def configure_routes(app: Flask) -> None:
        @app.route("/user", methods=["POST"])
        def create_user():
            name = request.json.get("name")
            if name:
                users[name] = name
                return {"data": f"User {name} is created!"}, 201
            return {"errors": {"name": "This field is required"}}, 422

        @app.route("/user/<name>", methods=["GET"])
        def get_user(name):
            if users.get(name):
                return {"data": f"My name is {name}"}, 200
            return "", 404

        @app.route("/user/<name>", methods=["PATCH"])
        def update_user(name):
            if users.get(name):
                new_name = request.json.get("name")
                users[name] = new_name
                return {"data": f"My name is {new_name}"}, 200
            return "", 404

        @app.route("/user/<name>", methods=["DELETE"])
        def delete_user(name):
            if users.get(name):
                users.pop(name)
                return "", 204
            return "", 404


if __name__ == "__main__":
    app.run(debug=True)
