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
        hiring_manager = data['hiring_manager']
        company_name = data['company_name']

    else:
        hiring_manager = request.form.get('hiring_manager')
        company_name = request.form.get('company_name')
    
    cover_letter = f"""Hi {hiring_manager}, I got your name and company info when you made a 
    POST request by clicking the 'Submit' button. Alternatively, you may have used the command 
    line to e.g., curl  -d 'hiring_manager=jade' -X POST http://127.0.0.1:5000/test, to get this response
    from the server. At any rate, I want to share with you what I have to offer as a developer 
    at {company_name}. """

    return render_template("cover_letter.html", hiring_manager = hiring_manager, company_name = company_name, cover_letter = cover_letter)
    # jsonify({'cover letter': cover_letter}) 

    


if __name__ == "__main__":
        app.run()