from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


def index():
    return render_template("index.html")


app.add_url_rule("/", view_func=index)


def main(settings):
    # Запусти здесь app.run, host и port возьми из settings.
    pass
