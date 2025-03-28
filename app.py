from flask import Flask, render_template, request

app = Flask(__name__)

def psw_check(psw):
    sp_char = "!@#$%^&*()+}{][?/:;-_"
    if (len(psw) >= 8 and
        any(char.isupper() for char in psw) and
        any(char.islower() for char in psw) and
        any(char.isdigit() for char in psw) and
        any(char in sp_char for char in psw)):
        return "Valid Password! You can use this"
    else:
        return "Invalid Password."

@app.route('/', methods=['GET', 'POST'])
def home():
    message = ""
    if request.method == 'POST':
        password = request.form['password']
        message = psw_check(password)
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
