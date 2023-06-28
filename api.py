from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mail import Mail, Message

app = Flask(__name__)
CORS(app)

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = "dclercqpeter@gmail.com"
app.config["MAIL_PASSWORD"] = "vhbwyynnuvwkwzmm"

mail = Mail(app)


@app.route("/send_email", methods=["POST"])
def send_email():
    data = request.get_json()
    name = data["name"]
    email = data["email"]
    phone = data["phone"]

    msg = Message(subject="Afspraak maken EPC",
                  sender="dcpeter.test.1@gmail.com",
                  recipients=[email])
    msg.body = f"Naam: {name}\n Email: {email}\n Phone: {phone}"
    print(msg)
    mail.send(msg)

    response = jsonify({"message": "Email verzonden!"})
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response
