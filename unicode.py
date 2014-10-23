from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/", methods=["POST","GET"])
def derp():
	if request.method == "POST":
		string = request.form["string"]
	else:
		string = ""
	if len(string) % 5 != 0:
		remainder = len(string) % 5
		for i in range(remainder):
			string= string+"0"
	divs = []
	for i in range(len(string.encode("hex"))/5):
		divs.append(string.encode("hex")[(i*5):(i*5)+5]+"0")

	return render_template("derp.html", divs=divs)
if __name__ == "__main__":
	app.run(debug=True, port=8080, host="0.0.0.0")