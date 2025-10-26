from flask import Flask, render_template, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "ridho_secret_key"
app.permanent_session_lifetime = timedelta(minutes=10)

@app.route('/', methods=['GET', 'POST'])
def index():
    if "history" not in session:
        session["history"] = []

    result = None
    error = None

    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operator = request.form['operator']

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    error = "Tidak bisa membagi dengan nol!"
                else:
                    result = num1 / num2
            else:
                error = "Operator tidak valid!"

            if error is None:
                # Simpan ke history
                calc_str = f"{num1} {operator} {num2} = {round(result, 3)}"
                history = session["history"]
                history.insert(0, calc_str)  # tampilkan dari yang terbaru
                session["history"] = history
        except ValueError:
            error = "Masukkan angka yang valid!"

    return render_template('index.html', result=result, error=error, history=session["history"])

@app.route('/clear')
def clear():
    session.pop("history", None)
    return render_template('index.html', result=None, error=None, history=[])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
