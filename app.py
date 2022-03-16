from flask import Flask ,render_template , request
from pred import anime_dundo_bc

app = Flask(__name__)


@app.route("/")
def index():
    return render_template ("index.html")



@app.route("/anime" , methods = ["POST","GET"])
def anime():
    if request.method == "POST":
        p = request.form["input"]
        n,g,r =anime_dundo_bc(p)
        return render_template ("anime.html", n=n , g =g, r =r)
    return render_template ("anime.html")


if __name__ == "__main__":
    app.run(debug=True)