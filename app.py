from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the endpoint for Dialogflow fulfillment
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    
    # Extract intent name from the request
    intent_name = req.get('queryResult', {}).get('intent', {}).get('displayName', '')

    # Handle different intents
    if intent_name == 'Requestservice':
        return handle_request_service(req)
    elif intent_name == 'ServicePaymentDetails':
        return handle_service_payment_details(req)
    else:
        return jsonify({'fulfillmentText': 'Sorry, I did not understand that.'})

def handle_request_service(req):
    # Extract parameters
    service_type = req.get('queryResult', {}).get('parameters', {}).get('service-type', '')

    # Logic to fetch and return service details based on service_type
    response_text = f"Here are the details for a {service_type} in your area."

    return jsonify({'fulfillmentText': response_text})

def handle_service_payment_details(req):
    # Extract parameters
    service_type = req.get('queryResult', {}).get('parameters', {}).get('service-type', '')

    # Logic to fetch and return payment details
    response_text = f"The average payment for a {service_type} is $X per hour."

    return jsonify({'fulfillmentText': response_text})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
