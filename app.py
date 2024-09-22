from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/printHello', methods=['GET'])
def printhello():
    return 'Hello World!!'

@app.route('/api/getJson', methods=['GET'])
def getjson():
    data = {
        'message': 'Hello World!!',
        
            "Response" : "json",
         
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
     