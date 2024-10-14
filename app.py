
@app.route('/process_message', methods=['POST'])
def process_message():
    data = request.get_json()
    user_message = data.get('message', '')
   
    # Add your logic to process the message (e.g., echo the message)
    bot_response = f"You said: {user_message}"

    return jsonify({'response': bot_response})

