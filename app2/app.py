from flask import Flask, render_template, request

app = Flask(__name__)

# Home route to serve the form
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form.get('name')
    color = request.form.get('color')
    return render_template('result.html', name=name, color=color)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
