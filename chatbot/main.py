from flask import Flask, render_template, request, jsonify
from chatbot_logic import get_answer

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/api/chatbot')
def chatbot():
    question = request.args.get('question', '').strip().lower()
    if not question:
        return jsonify({'answer': 'Please ask a question.'})

    try:
        answer = get_answer(question)
        return jsonify({'answer': answer})
    except Exception as e:
        print('Error:', e)
        return jsonify({'answer': 'Server error. Try again later.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
