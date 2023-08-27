from flask import Flask, request, jsonify
import sqlite3

app = Flask(_name_)

# Initialize SQLite database
conn = sqlite3.connect('operations.db')
cursor = conn.cursor()

# Create history table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY,
        operation TEXT,
        result INTEGER
    )
''')
conn.commit()

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

@app.route('/evaluate/<path:operation>', methods=['GET'])
def evaluate(operation):
    try:
        parts = operation.split('/')
        operands = [int(parts[i]) for i in range(0, len(parts), 2)]
        operators = [parts[i] for i in range(1, len(parts), 2)]
        result = perform_operation(operands, operators)
        
        # Store operation in history database
        cursor.execute('INSERT INTO history (operation, result) VALUES (?, ?)', (operation, result))
        conn.commit()
        
        return jsonify({'question': operation, 'answer': result})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/history', methods=['GET'])
def history():
    try:
        cursor.execute('SELECT operation, result FROM history ORDER BY id DESC LIMIT 20')
        history_data = [{'question': row[0], 'answer': row[1]} for row in cursor.fetchall()]
        return jsonify({'history': history_data})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.teardown_appcontext
def close_connection(exception):
    conn.close()

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
