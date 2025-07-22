from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello World</h1>"


@app.route("/about")
def about():
    return "<h1>About Page</h1>"


# Different https parameters
@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        return jsonify({"message": "GET request received"})
    elif request.method == "POST":
        data = request.get_data()
        print(data)
        return jsonify({"message": "CREATE USER"})
    else:
        return jsonify({"message": "Method not allowed"})


# URL parameters
@app.route("/users/<string:username>")
def show_user(usernmae):
    return f"<h1>User: {usernmae}</h1>"


# Query Parameters
@app.route("/search")
def search():
    query = request.args.get("q", "")
    category = request.args.get("category", "all")
    sort_by = request.args.get("sort", "relevance")

    return f"""
    <h1>Search results for: {query}</h1>
    <p>Category: {category}</p>
    <p>Sort by: {sort_by}</p>
    """


# Request Data
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name", "Guest")
    email = request.form.get("email", "guest@example.com")
    return f"<h1>Name: {name}</h1><h1>Email: {email}</h1>"


@app.before_request
def before_request():
    print("Before request")


@app.after_request
def after_request(response):
    print("After request")
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
