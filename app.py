from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'service': 'NovaMart Online',
        'version': '2.0',
        'status': 'running',
        'message': 'Welcome to NovaMart Service!'
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

@app.route('/api/products')
def products():
    return jsonify({
        'products': [
            {'id': 1, 'name': 'Product A', 'price': 29.99},
            {'id': 2, 'name': 'Product B', 'price': 49.99},
            {'id': 3, 'name': 'Product C', 'price': 19.99}
        ]
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)