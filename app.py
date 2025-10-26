from flask import Flask, render_template, request, session, jsonify
from datetime import timedelta
import math

app = Flask(__name__)
app.secret_key = "ridho_secret_key"
app.permanent_session_lifetime = timedelta(minutes=10)

@app.route('/')
def index():
    if "history" not in session:
        session["history"] = []
    return render_template('index.html', history=session["history"])

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.json.get('expression', '')
    try:
        # evaluasi ekspresi dengan aman
        result = eval(expression, {"__builtins__": None}, {"math": math})
        calc_str = f"{expression} = {round(result, 3)}"
        history = session.get("history", [])
        history.insert(0, calc_str)
        session["history"] = history
        return jsonify(success=True, result=result, history=history)
    except Exception:
        return jsonify(success=False, error="Ekspresi tidak valid!")

@app.route('/clear', methods=['POST'])
def clear():
    session.pop("history", None)
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
