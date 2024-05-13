from flask import request, render_template
from app import app
from app.html_generator import HTMLGenerator


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
        
    json_data = request.form.get('json_data')

    if json_data:
        html_generator = HTMLGenerator(json_data)
        return html_generator.generate_html()
    else:
        return "No JSON data provided!", 400