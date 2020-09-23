from flask import Flask, escape, request

app = Flask(__name__)

def suma(a,b):
    return a+b

@app.route('/')
def hello():
    res = suma (3,2)
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}! %s' % (res)
#    return "Hello Wolrd!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
