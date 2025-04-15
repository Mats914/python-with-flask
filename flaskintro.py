from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bakverk')
def bakverk():
    return render_template('bakverk.html')

@app.route('/bestallningar')
def bestallningar():
    return render_template('bestallningar.html')

@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')

@app.route('/om-oss')
def om_oss():
    return render_template('om-oss.html')

if __name__ == '__main__':
    app.run(debug=True)
