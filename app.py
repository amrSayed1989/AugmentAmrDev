from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json.get('message', '').lower() # Get message and convert to lowercase

    if not user_message:
        ai_reply = "AI Coder: I didn't receive a message. Please type something!"
    elif 'hello' in user_message or 'hi' in user_message:
        ai_reply = "AI Coder: Hello! I am the AI Coder. How can I help you with your code today?"
    elif 'python' in user_message:
        ai_reply = "AI Coder: Python is a powerful language! What specific Python topic are you interested in (e.g., lists, functions, Flask)?"
    elif 'javascript' in user_message or 'js' in user_message:
        ai_reply = "AI Coder: JavaScript is great for web development! Are you working on frontend or backend (Node.js) JavaScript?"
    elif 'java' in user_message:
        ai_reply = "AI Coder: Java is a robust language, often used for enterprise applications. What part of Java are you curious about?"
    elif 'help' in user_message:
        ai_reply = "AI Coder: I can try to help with questions about Python, JavaScript, or Java. What's your question?"
    else:
        ai_reply = "AI Coder: Interesting point. I can currently provide basic information on Python, JavaScript, and Java. What would you like to discuss?"
        
    return jsonify({'reply': ai_reply})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
