from flask import Flask, request, jsonify

app = Flask()

# Route to accept POST requests from another page
@app.route('/submit-data', methods=['POST'])
def submit_data():
    received_data = request.json  # Getting JSON data from the request
    print('Data received:', received_data)

    # Sending a response back to the requester
    return jsonify({
        'message': 'Request received successfully',
        'data': received_data
    })

if name == 'main':
    app.run(debug=True, port=5000)