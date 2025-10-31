📨 Flask Email Verification App

A simple email verification web app built using Flask and Flask-Mail.

It allows users to enter their email, receive an OTP, and verify it — perfect for learning authentication and mail handling in Flask.



🚀 Features

* Send OTP via Gmail using Flask-Mail
* Verify OTP in a separate form
* Bootstrap 5 UI (clean, modern design)
* Flash messages for user feedback
* Session-based OTP validation



🏗️ Project Structure

Flask\_Email\_Verification/

│

├── app.py                # Main Flask application

├── requirements.txt      # Project dependencies

├── README.md             # Project info

└── templates/            # HTML templates

    ├── index.html        # Email input form

    └── verify.html       # OTP verification form



⚙️ Installation

1\. Clone this repository:

git clone https://github.com/<your-username>/Flask\_Email\_Verification.git

cd Flask\_Email\_Verification



2\. Install dependencies:

pip install -r requirements.txt



3\. Open app.py and update:

app.config\["MAIL\_USERNAME"] = "your\_email@gmail.com"

app.config\["MAIL\_PASSWORD"] = "your\_app\_password"



4\. Run the app:

python app.py



5\. Visit:

http://127.0.0.1:5000



🧠 How It Works

1. User enters their email on the home page.
2. A random 6-digit OTP is generated.
3. OTP is sent via Gmail using your app password.
4. User enters OTP on the next screen to verify.



🔐 App Password Setup (Required for Gmail)



1. Turn on 2-Step Verification in your Google Account.
2. Go to App Passwords.
3. Select Mail and Other (Flask App) → Generate.
4. Copy the 16-character code and use it in your app.



🧾 License

This project is open-source and available under the MIT License.



✨ Author

Ashish Santosh Khote

📧 ashishkhoteak47@gmail.com

💻 GitHub: eshuuuux



