from flask import Flask, request, jsonify
from chain import RamblaChain

app = Flask(__name__)

ALLOWED_USERS_FILE = 'allowed_users'
with open(ALLOWED_USERS_FILE) as f:
    allowed_users = [l.strip() for l in f.readlines()]

chains_per_device = {}


@app.route('/start', methods=['POST'])
def start_game():
    data = request.json
    device_id = data.get('deviceId')

    if not device_id:
        return jsonify({"error": "Missing required data"}), 400

    #   if username not in allowed_users:
    #       return jsonify({"error": "Unauthorized"}), 403

    chains_per_device[device_id] = RamblaChain()
    return jsonify(), 200


@app.route('/input', methods=['POST'])
def handle_input():
    data = request.json
    device_id = data.get('deviceId')
    user_input = data.get('input')

    if not device_id or not user_input:
        return jsonify({"error": "Missing required data"}), 400

    #   if username not in allowed_users:
    #       return jsonify({"error": "Unauthorized"}), 403

    chain = chains_per_device.get(device_id)
    if not chain:
        chain = RamblaChain()
        chains_per_device[device_id] = chain

    next_questions = chain.interact(user_input)

    return jsonify({"questions": next_questions}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9999)
