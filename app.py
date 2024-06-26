from flask import Flask, render_template, jsonify
from flask import send_file, redirect, request
from flask import url_for, make_response, abort

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/download')
def download_file():
    return send_file('static/file.txt', as_attachment=True)

@app.route('/redirect')
def go_to_about():
    return redirect(url_for('about'))

@app.route('/custom')
def custom_response():
    response = make_response("Custom Response", 200)
    response.headers['Custom-Header'] = 'CustomValue'
    return response

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        "message": "This is your data!",
        "status": "success"
    }
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def post_data():
    if request.is_json:
        data = request.get_json()
        response = {
            "message": "Data received!",
            "data": data
        }
        return jsonify(response), 201
    else:
        return jsonify({"error": "Request must be JSON"}), 400

@app.route('/error')
def error():
    abort(404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
        
