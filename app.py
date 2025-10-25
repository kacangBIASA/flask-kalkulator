from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
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
        except ValueError:
            error = "Masukkan angka yang valid!"
    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
