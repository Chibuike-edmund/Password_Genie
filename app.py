from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length=20):
    characters = string.ascii_letters + string.digits 
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    length = int(request.form.get("length", 20))
    password = generate_password(length)
    return render_template("result.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)
