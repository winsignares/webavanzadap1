from bd import app, db
from model.Articulos import Articulo, ArticuloSchema 
from flask import Flask,jsonify
import json


articulo_schema = ArticuloSchema()
articulos_schema = ArticuloSchema(many=True)

@app.route('/', methods=['GET'])
def indexarticulo():
    all_tasks = Articulo.query.all()
    result = articulos_schema.dump(all_tasks)
    print(all_tasks)
    for item in all_tasks:
        print(item)
    return json.dumps(result)
    #jsonify(result)
    
    #for item in result:
    #    print(item)
    
    #return jsonify(result)  

if __name__ == "__main__":
    app.run(debug=True)
