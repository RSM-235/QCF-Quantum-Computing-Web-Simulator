from flask import Flask, request, render_template_string
import subprocess

app = Flask(__name__)

HTML = open("index.html").read()

@app.route("/")
def home():
    return HTML

@app.route("/run", methods=["POST"])
def run():
    func = request.form.get("function")
    params = request.form.get("params")

    cmd = f"cd .. && octave --quiet --eval '{func}({params})'"

    try:
        result = subprocess.getoutput(cmd)
    except Exception as e:
        result = str(e)

    return f"<pre>{result}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
