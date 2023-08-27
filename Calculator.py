from flask import Flask, request, jsonify

app = Flask(_name_)

operations_history = []  # To store the last 20 operations

def calculate_expression(expression):
    try:
        expression = expression.replace('/plus/', '+').replace('/minus/', '-').replace('/into/', '*').replace('/by/', '/')
        result = eval(expression)
        return result
    except Exception as e:
        return str(e)

@app.route('/', methods=['GET'])
def index():
    return "Welcome to the Calculator App!"

@app.route('/evaluate/<path:expression>', methods=['GET'])
def evaluate(expression):
    try:
        result = calculate_expression(expression)
        operations_history.append({'question': expression, 'answer': result})
        
        if len(operations_history) > 20:
            operations_history.pop(0)  # Remove the oldest operation if history exceeds 20
            
        return jsonify({'question': expression, 'answer': result})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/history', methods=['GET'])
def history():
    return jsonify(operations_history)

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
