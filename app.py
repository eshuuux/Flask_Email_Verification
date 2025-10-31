from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mail import Mail, Message
import random

app = Flask(__name__)
app.secret_key = "romify_secret_key"  # Needed for session

# -------- MAIL CONFIG --------
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True

# 🟢 ENTER YOUR DETAILS HERE
app.config["MAIL_USERNAME"] = "your@gmail.com" # your gmail
app.config["MAIL_PASSWORD"] = "*********"     # 16-digit App Password

mail = Mail(app)

# -------- ROUTES --------
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        email = request.form["email"]
        otp = str(random.randint(100000, 999999))
        session["otp"] = otp
        session["email"] = email

        msg = Message("Your OTP Code - Romify", sender=app.config["MAIL_USERNAME"], recipients=[email])
        msg.body = f"Hello!\nYour OTP code is: {otp}\n\nIt will expire in 5 minutes."
        mail.send(msg)

        flash("OTP sent to your email!", "info")
        return redirect(url_for("verify"))
    return render_template("index.html")

@app.route("/verify", methods=["GET", "POST"])
def verify():
    if request.method == "POST":
        user_otp = request.form["otp"]
        if user_otp == session.get("otp"):
            flash("✅ Email verified successfully!", "success")
            return redirect(url_for("index"))
        else:
            flash("❌ Invalid OTP! Try again.", "danger")
    return render_template("verify.html")

if __name__ == "__main__":
    app.run(debug=True)
