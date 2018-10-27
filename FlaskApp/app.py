
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')	

@app.route("/main.html")

def home():
	return render_template('main.html')

@app.route("/social.html")

def social():
	return render_template('social.html')
if __name__ == "__main__":
    app.run()
