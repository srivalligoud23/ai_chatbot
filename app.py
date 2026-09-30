from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form["message"]

    # Simple chatbot responses
    message = user_message.lower()

    if "hello" in message or "hi" in message:
        response = "Hello! How can I help you?"
    elif "how are you" in message:
        response = "I'm doing great! Thank you for asking."
    elif "bye" in message:
        response = "Goodbye! Have a great day!"
    else:
        response = "I'm still learning. Please ask me another question."

    return response


if __name__ == "__main__":
    app.run(debug=True)