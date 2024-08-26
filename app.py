from flask import Flask, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/time', methods=['GET'])
def get_current_time():
    # Set the timezone to West Africa Time (WAT)
    wat_timezone = pytz.timezone('Africa/Lagos')  # Lagos, Nigeria is in WAT
    current_time = datetime.now(wat_timezone)
    
    # Format the time as a string
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S %Z')
    
    # Return the time in JSON format
    return jsonify({'current_time': formatted_time})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
