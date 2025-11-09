from flask import Flask, render_template,request, redirect, url_for, session, jsonify, request

app = Flask(__name__)
app.secret_key = "supersecretkey"  # required for session management

APP_PASSWORD = "network010"

@app.route('/')
def home():
    # Redirect to login if not logged in
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        password = request.form.get("password")
        if password == APP_PASSWORD:
            session["logged_in"] = True
            return redirect(url_for("home"))
        else:
            return render_template("login.html", error="Incorrect password.")
    return render_template("login.html")

@app.route('/logout')
def logout():
    session["logged_in"] = False
    return redirect(url_for("login"))


@app.route('/monthly')
def monthly():
    return render_template('monthly.html')

@app.route('/map')
def map_page():
    return render_template('map.html')

@app.route('/graphs')
def graphs():
    return render_template('graphs.html')


@app.route('/punjab')
def punjab_page():
    return render_template('punjab.html')

#--------------#
#Calendar Data
#--------------#

@app.route('/calendar')
def calendar_page():
    return render_template('calendar.html')

events = [
    {"title": "meeting", "start": "2025-11-07"},
    
]
@app.route('/events')
def get_events():
    """Send all events to the frontend as JSON."""
    return jsonify(events)

    
@app.route('/add_event', methods=['POST'])
def add_event():
    """Receive new event data from frontend and add to events list."""
    data = request.get_json()
    events.append(data)
    return jsonify({"status": "success"}), 200


if __name__ == '__main__':
    app.run(debug=True)
