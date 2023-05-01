from app import app


@app.route("/")
def index():
    return "Hello from Flask!!"

@app.route("/name")
def name():
    return "<h1>Masila David Mwendwa!!</h1>"