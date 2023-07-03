from flask import Flask, render_template, request, jsonify
import process
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message', methods=['POST'])
def message():
    user_message = request.form['text']
    # Process the user's message and generate a response
    bot_message = process.process_text(user_message)
    response = {'message': bot_message}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
