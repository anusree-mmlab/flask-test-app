from flask import Flask

app = Flask(__name__)
print(__name__)

@app.route('/')
def op():
    return 'Hello d'

if __name__ == '__main__':
    app.run(debug=True)    
    