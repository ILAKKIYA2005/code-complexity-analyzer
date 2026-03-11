from flask import Flask, render_template, request
from analyzer import analyze_code

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    result = None

    if request.method == "POST":

        language = request.form["language"]

        # check if file uploaded
        file = request.files.get("file")

        if file and file.filename != "":
            code = file.read().decode("utf-8")
        else:
            code = request.form["code"]

        result = analyze_code(code, language)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)