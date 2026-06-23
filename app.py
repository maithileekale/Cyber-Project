from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("models/ids_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    duration = float(request.form["duration"])
    src_bytes = float(request.form["src_bytes"])
    dst_bytes = float(request.form["dst_bytes"])

    sample = [[
        duration,1,1,1,
        src_bytes,dst_bytes,
        0,0,0,0,0,1,0,0,0,0,0,0,0,0,
        0,0,2,2,0,0,0,0,1,0,0,
        150,25,0.17,0.03,0.17,0,0,0,0.05,0,
        20
    ]]

    prediction = model.predict(sample)

    # Demo Visualization Logic
    if src_bytes > 100000 or dst_bytes > 500000:

        result = "ATTACK DETECTED"
        risk = "HIGH"
        color = "danger"
        icon = "🚨"

        threat_type = "DDoS / Network Flooding"

        recommendation = """
        Block suspicious IP addresses,
        enable firewall rules,
        and monitor traffic patterns.
        """

    else:

        result = "NORMAL TRAFFIC"
        risk = "LOW"
        color = "success"
        icon = "✅"

        threat_type = "No Threat Detected"

        recommendation = """
        Network traffic is operating normally.
        Continue regular monitoring.
        """

    return render_template(
        "result.html",
        result=result,
        risk=risk,
        color=color,
        icon=icon,
        threat_type=threat_type,
        recommendation=recommendation
    )

if __name__ == "__main__":
    app.run(debug=True)