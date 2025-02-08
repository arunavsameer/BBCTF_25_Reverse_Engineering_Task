from flask import Flask, request
import os

app = Flask(__name__)

# Read from environment variables
FLAG = os.getenv("FLAG", "FLAG{default_flag}")
CORRECT_PASSWORD = os.getenv("PASSWORD", "default")
OBFUSCATED_PASSWORD = "ba 60 a7 ee 1c 73 90 cf 47 9a 17"

@app.route("/")
def home():
    return "Welcome to the Reverse Engineering Challenge!\n"

@app.route("/challenge", methods=["GET", "POST"])
def challenge():
    if request.method == "GET":
        return f"The obfuscated password is: {OBFUSCATED_PASSWORD}\nEnter the correct password: "

    # Handle user input
    user_input = request.form.get("password", "").strip()

    if user_input == CORRECT_PASSWORD:
        return f"Correct! Here is your flag: {FLAG}\n"
    else:
        return "Incorrect password! Try again.\n"

if __name__ == "__main__":
    PORT = int(os.getenv("PORT", 5000))  # Railway assigns this
    app.run(host="0.0.0.0", port=PORT)
