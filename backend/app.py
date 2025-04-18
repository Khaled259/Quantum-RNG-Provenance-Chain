from flask import Flask, render_template, jsonify, request
import subprocess, json, joblib
from quantum.random_bits import generate_random_bits, hash_batches

app = Flask(__name__)
model = joblib.load('../ai/model.pkl')

@app.route('/')
def index():
    bits = generate_random_bits(256)
    hashes = hash_batches(bits)
    health = model.predict([list(map(int, bits))])[0]
    return render_template('index.html', bits=bits, hash=hashes[0], health=health)

@app.route('/api/random')
def api_random():
    bits = generate_random_bits(256)
    h = hash_batches(bits)[0]
    return jsonify(bits=bits, hash=h)

if __name__ == '__main__':
    app.run(debug=True)
