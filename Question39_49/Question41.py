from flask import Flask

app = Flask(__name__)

@app.route('/display/<string:message>')
def display_message(message):
    message= 'I like pizza'
    return f'<h1>{message}</h1>'

if __name__ == '__main__':
    app.run(debug=True)
