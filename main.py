from flask import Flask, render_template, request
from ai_utils import generate_ad_copy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/generate_ad', methods=['POST'])
def generate_ad():
    practice_area = request.form['practice_area']
    location = request.form['location']
    ad = generate_ad_copy(practice_area, location)
    return render_template('dashboard.html', ad_copy=ad)

if __name__ == '__main__':
    app.run(debug=True)
