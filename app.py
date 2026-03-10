from flask import Flask, render_template, request
from analyzer import analyze_code

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():

    result=""
    complexity=""

    if request.method=="POST":

        code=request.form["code"]
        language=request.form["language"]

        result=analyze_code(code,language)

        if "O(1)" in result:
            complexity="constant"

        elif "O(n)" in result:
            complexity="linear"

        elif "O(n^2)" in result:
            complexity="quadratic"

        else:
            complexity="cubic"

    return render_template("index.html",result=result,complexity=complexity)

if __name__=="__main__":
    app.run(debug=True)