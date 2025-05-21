import unittest
import json
from app import app # Assuming your Flask app instance is named 'app' in app.py

class ChatAppTests(unittest.TestCase):

    def setUp(self):
        app.testing = True # Set testing mode before creating the test client
        self.app = app.test_client()
        

    def test_send_message_hello(self):
        payload = json.dumps({'message': 'hello'})
        response = self.app.post('/send_message', 
                                 headers={'Content-Type': 'application/json'},
                                 data=payload)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['reply'], "AI Coder: Hello! I am the AI Coder. How can I help you with your code today?")

    def test_send_message_hi(self):
        payload = json.dumps({'message': 'hi there'})
        response = self.app.post('/send_message', 
                                 headers={'Content-Type': 'application/json'},
                                 data=payload)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['reply'], "AI Coder: Hello! I am the AI Coder. How can I help you with your code today?")

    def test_send_message_python(self):
        payload = json.dumps({'message': 'tell me about python'})
        response = self.app.post('/send_message', 
                                 headers={'Content-Type': 'application/json'},
                                 data=payload)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['reply'], "AI Coder: Python is a powerful language! What specific Python topic are you interested in (e.g., lists, functions, Flask)?")

    def test_send_message_javascript(self):
        payload = json.dumps({'message': 'what is javascript?'})
        response = self.app.post('/send_message', 
                                 headers={'Content-Type': 'application/json'},
                                 data=payload)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['reply'], "AI Coder: JavaScript is great for web development! Are you working on frontend or backend (Node.js) JavaScript?")

    def test_send_message_js(self):
        payload = json.dumps({'message': 'explain js'})
        response = self.app.post('/send_message', 
                                 headers={'Content-Type': 'application/json'},
                                 data=payload)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['reply'], "AI Coder: JavaScript is great for web development! Are you working on frontend or backend (Node.js) JavaScript?")

    def test_send_message_java(self):
        payload = json.dumps({'message': 'I have a question about java'})
        response = self.app.post('/send_message', 
                                 headers={'Content-Type': 'application/json'},
                                 data=payload)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['reply'], "AI Coder: Java is a robust language, often used for enterprise applications. What part of Java are you curious about?")

    def test_send_message_help(self):
        payload = json.dumps({'message': 'can you help me?'})
        response = self.app.post('/send_message', 
                                 headers={'Content-Type': 'application/json'},
                                 data=payload)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['reply'], "AI Coder: I can try to help with questions about Python, JavaScript, or Java. What's your question?")

    def test_send_message_generic(self):
        payload = json.dumps({'message': 'What is the weather like?'})
        response = self.app.post('/send_message', 
                                 headers={'Content-Type': 'application/json'},
                                 data=payload)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['reply'], "AI Coder: Interesting point. I can currently provide basic information on Python, JavaScript, and Java. What would you like to discuss?")

    def test_send_message_empty(self):
        payload = json.dumps({'message': ''})
        response = self.app.post('/send_message', 
                                 headers={'Content-Type': 'application/json'},
                                 data=payload)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['reply'], "AI Coder: I didn't receive a message. Please type something!")

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<title>AI Coder Chat</title>', response.data)

if __name__ == '__main__':
    unittest.main()
