# Load Test: Verify the endpoints from VM using port-forwarding and curl
# Load Test: Verified the endpoint /home in CMD using cURL

from flask import Flask, request, jsonify
from prometheus_client import Counter, generate_latest
import os

app = Flask(__name__)
notes = {}
API_KEY = os.getenv("API_KEY", "demo123")
REQ_COUNTER = Counter("http_requests_total", "Total HTTP Requests")

@app.before_request
def count_requests():
    REQ_COUNTER.inc()

@app.route("/notes", methods=["GET"])
def get_all_notes():
    return jsonify(notes)

@app.route("/notes/<note_id>", methods=["GET"])
def get_note(note_id):
    note = notes.get(note_id)
    if not note:
        return jsonify({"error": "Note not found"}), 404
    return jsonify({note_id: note})

@app.route("/notes", methods=["POST"])
def create_note():
    if request.headers.get("X-Key") != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401
    body = request.json
    note_id = body.get("note_id")
    text = body.get("text", "")
    if not note_id:
        return jsonify({"error": "Missing note_id"}), 400
    if note_id in notes:
        return jsonify({"error": "Note already exists"}), 409
    notes[note_id] = text
    return jsonify({"status": "created", "note_id": note_id})

@app.route("/notes/<note_id>", methods=["PUT"])
def update_note(note_id):
    if request.headers.get("X-Key") != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401
    if note_id not in notes:
        return jsonify({"error": "Note not found"}), 404
    notes[note_id] = request.json.get("text", notes[note_id])
    return jsonify({"status": "updated", "note_id": note_id})

@app.route("/notes/<note_id>", methods=["DELETE"])
def delete_note(note_id):
    if request.headers.get("X-Key") != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401
    if note_id not in notes:
        return jsonify({"error": "Note not found"}), 404
    notes.pop(note_id)
    return jsonify({"status": "deleted", "note_id": note_id})

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/metrics")
def metrics():
    return generate_latest()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



