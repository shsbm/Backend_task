from flask import Flask, request, jsonify

app = Flask(__name__)

operations_history = []

def perform_operation(operands, operators):
    result = operands[0]
    for i in range(len(operators)):
        if operators[i] == "plus":
            result += operands[i + 1]
        elif operators[i] == "minus":
            result -= operands[i + 1]
        elif operators[i] == "into":
            result *= operands[i + 1]
    return result

@app.route('/', methods=['GET'])
def index():
    return "Welcome to the Calculator App!"

@app.route('/calculate', methods=['GET'])
def calculate():
    try:
        operation = request.args.get('operation')
        parts = operation.split('/')
        
        operands = [int(parts[i]) for i in range(1, len(parts), 2)]
        operators = [parts[i] for i in range(2, len(parts), 2)]
        
        result = perform_operation(operands, operators)
        operations_history.append({'question': operation, 'answer': result})
        
        if len(operations_history) > 20:
            operations_history.pop(0)
        
        return jsonify({'question': operation, 'answer': result})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/history', methods=['GET'])
def history():
    return jsonify({'history': operations_history})

if __name__ == '__main__':
    app.run()
