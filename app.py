from flask import Flask, request, jsonify, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    result = subprocess.run(['python', 'sherlock/sherlock.py', query, '--print-found'], 
                            capture_output=True, text=True)
    return jsonify({"result": result.stdout if result.stdout else "Koi profile nahi mili"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
