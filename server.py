from flask import Flask, render_template, request, jsonify
import json 

app = Flask(__name__)


@app.route('/')
def index():
    """This is a home page."""

    return render_template("home.html")
    

@app.route('/test')
def show_form():
    """Ask for string_to_cut."""

    return render_template("test.html")

@app.route('/test', methods=['POST'])
def generate_return_string():
    """Take string_to_cut and generate return_string."""

    if request.json:
        data = request.json
        string_to_cut = data["string_to_cut"]

    else:
        string_to_cut = request.form.get('string_to_cut')

    return_string = ""
    current = 2

    for i in range(0, len(string_to_cut)):
        if current + 3 <= len(string_to_cut):
            return_string += string_to_cut[current]
            current = current + 3
        else:
            return jsonify({'return string': return_string})

    return jsonify({'return string': return_string})
    


if __name__ == "__main__":
        app.run()