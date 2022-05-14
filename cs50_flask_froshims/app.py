from flask import Flask, render_template, request

app=Flask(__name__)
sports=["Basketball","Football","Cricket"]
Registrations={}

@app.route("/")
def index():
    return render_template("index.html",sports=sports)

@app.route("/register", methods=["POST"])
def register():

    if not request.form.get("name") or  request.form.get("sport") not in sports:
        return render_template("failure.html")

    return render_template("success.html") 

if __name__ == '__main__':
    app.run(debug=True)