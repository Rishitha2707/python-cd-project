from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

visit_count = 0

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    data = request.get_json()
    name = data.get('name', 'Guest')
    return jsonify({"message": f"Hello {name} 👋 Welcome to K8s!"})

@app.route('/count', methods=['GET'])
def count():
    global visit_count
    visit_count += 1
    return jsonify({"count": visit_count})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
