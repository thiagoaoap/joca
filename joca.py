from flask import render_template, Flask

app = Flask(__name__)


@app.route('/')
def pagina_home():
    return render_template('joca.html')


if __name__ == "__main__":
    app.run(port=8000, debug=True)