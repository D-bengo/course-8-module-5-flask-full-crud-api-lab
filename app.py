from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# POST /events - Create a new event
@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()

    # Validate input
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    # Create new event ID
    new_id = events[-1].id + 1 if events else 1

    # Create and store event
    new_event = Event(new_id, data["title"])
    events.append(new_event)

    return jsonify({
        "message": "Event created successfully",
        "event": new_event.to_dict()
    }), 201


# PATCH /events/<id> - Update event title
@app.route('/events/<int:id>', methods=['PATCH'])
def update_event(id):
    data = request.get_json()

    # Find event
    event = next((e for e in events if e.id == id), None)

    if event is None:
        return jsonify({"error": "Event not found"}), 404

    # Validate input
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    # Update title
    event.title = data["title"]

    return jsonify({
        "message": "Event updated successfully",
        "event": event.to_dict()
    }), 200


# DELETE /events/<id> - Remove event
@app.route('/events/<int:id>', methods=['DELETE'])
def delete_event(id):
    global events

    # Find event
    event = next((e for e in events if e.id == id), None)

    if event is None:
        return jsonify({"error": "Event not found"}), 404

    # Remove event
    events = [e for e in events if e.id != id]

    return jsonify({
        "message": "Event deleted successfully"
    }), 200


if __name__ == "__main__":
    app.run(debug=True)