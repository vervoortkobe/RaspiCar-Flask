from flask import Flask, render_template, jsonify
from services.raspberry_service import Raspberry_service 

app = Flask(__name__)
service = Raspberry_service()

@app.route('/controller')
def get_controller():
    return render_template('controller.html')

@app.route('/api/enable-led', methods=['POST'])
def enable_led():
    try:
        service.turn_on_led()
        return jsonify({'message': 'LED enabled successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    
@app.route('/api/disable-led', methods=['POST'])
def disable_led():
    try:
        service.turn_off_led()
        return jsonify({'message': 'LED enabled successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/api/press-forward', methods=['POST'])
def press_forward():
    try:
        service.press_forward()
        return jsonify({'message': 'successfull'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/api/release-forward', methods=['POST'])
def release_forward():
    try:
        service.release_forward()
        return jsonify({'message': 'successfull'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/api/press-backward', methods=['POST'])
def press_backward():
    try:
        service.press_backward()
        return jsonify({'message': 'successfull'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/api/release-backward', methods=['POST'])
def release_backward():
    try:
        service.release_backward()
        return jsonify({'message': 'successfull'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/api/press-right', methods=['POST'])
def press_right():
    try:
        service.press_right()
        return jsonify({'message': 'successfull'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/api/release-right', methods=['POST'])
def release_right():
    try:
        service.release_right()
        return jsonify({'message': 'successfull'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/api/press-left', methods=['POST'])
def press_left():
    try:
        service.press_left()
        return jsonify({'message': 'successfull'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/api/release-left', methods=['POST'])
def release_left():
    try:
        service.release_left()
        return jsonify({'message': 'successfull'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0')
