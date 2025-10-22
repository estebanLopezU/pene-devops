from flask import flask, request, jsonify

app = Flask(__name__)

@app.route('/suma', methods=['GET'])
def suma():
    a= int(request.args.get('a',0))
    b= int(request.args.get('b',0))
    result= a+b
    return jsonify({'resultado':result})
@app.route('/multiplica', methods=['POST'])
def multiplicar():
    datos = request.get_json()
    a= datos.get('a',1)
    b= datos.get ('b',1)
    result= a*b
    return jsonify({'resultado':result})
if__name__='__main__':
    app.run(debug-True)
