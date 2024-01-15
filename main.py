from flask import Flask, request

app = Flask(__name__)

# @app.route('/')
# def index():
# 	return 'Hello World!'

@app.route('/', methods=['POST'])
def result():
    print(request.data)  # raw data
    print(request.json)  # json (if content-type of application/json is sent with the request)
    print(request.get_json(force=True))  # json (if content-ty

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=10000, debug=False)
