from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['POST'])
def result():
    f = open("log.txt", "a+")
    f.write(request.form['data'])
    f.close()

if __name__ == "__main__":
	# App config.
	app.config.from_object(__name__)

	#Allows server to be hosted externally
	app.run(host='0.0.0.0')
