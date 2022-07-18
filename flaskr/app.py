from flask import Flask, render_template
import scripts

app = Flask(__name__)

@app.route("/")
def index():
    data = scripts.get_json_data()
    return render_template("index.html", data=data)


@app.route("/history")
def history():
    return render_template("history.html")


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

@app.context_processor
def context_processor():
    time = scripts.get_footer_time()
    return dict(time=time)


if __name__ == "__main__":
    app.run(debug=True)
