from flask import Flask, render_template, request

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return '''
    <h2><center>Hello</center></h2>
    <center>
        <a href="/register">Go to Registration Page</a>
    </center>
    '''

# Registration Page
@app.route('/register')
def register():
    return render_template('register.html')

# Success Page
@app.route('/success', methods=['POST'])
def success():
    name = request.form['name']
    year = request.form['year']

    return render_template('success.html', name=name, year=year)

if __name__ == '__main__':
    app.run(debug=True)
