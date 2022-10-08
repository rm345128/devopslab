from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "rm345128, Hello World!"

if __name__ == '__main__':
    app.run()