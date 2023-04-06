from flask import Flask, render_template

app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')

# Define the about route
@app.route('/about')
def about():
    return render_template('index.html')

# Define the services route
@app.route('/services')
def services():
    return render_template('index.html')

# Define the projects route
@app.route('/projects')
def projects():
    return render_template('index.html')

# Define the contact us route
@app.route('/contact-us')
def contact_us():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
