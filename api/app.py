from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import psycopg2 as pg
from psycopg2.extras import DictCursor
import json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins":"*"}})

#@cross_origin(allow_headers=['Content-Type'], origins="*")
#@cross_origin()
@app.route("/", methods=['POST','GET'])
def hello():
    conn = pg.connect(database='postgres', user='postgres', host='db', password='docker')
    db = conn.cursor(cursor_factory=DictCursor)

    db.execute("SELECT * from TODOS")
    rows = [dict(record) for record in db] #db.fetchall()

    conn.close()
    return jsonify(rows)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
