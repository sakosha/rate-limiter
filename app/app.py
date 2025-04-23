from __future__ import annotations

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello() -> str:
    return "Hello world!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
