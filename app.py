
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]

        return f"""
        <h2>Registration Successful!</h2>
        <p>Name: {name}</p>
        <p>Email: {email}</p>
        """

    return """
    <h2>User Registration Form</h2>
    <form method="POST">
        Name: <input type="text" name="name" required><br><br>
        Email: <input type="email" name="email" required><br><br>
        <button type="submit">Register</button>
    </form>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
