from flask import Flask,jsonify,request
app = Flask(__name__)
from datetime import datetime

from flaskext.mysql import MySQL
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'blog_flask'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL()
mysql.init_app(app)

@app.route('/example')
def index():
    return 'hello world'

class EqltByGene(object):
    def serialize(self):
        return {
            'gene_id': self.gene_id, 
            'gene_symbol': self.gene_symbol,
            'p_value': self.p_value,
        }

@app.route('/randompost', methods = ['POST','GET'])
def get_or_post_data():    
    if request.method == 'GET':
        conn = mysql.connect()
        cursor = conn.cursor()
        #q_create_table = "CREATE TABLE IF NOT EXISTS RANDOMPOST (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,first VARCHAR(20) NOT NULL,second VARCHAR(20) NOT NULL,creation_date TIMESTAMP)";
        #cursor.execute(q_create_table)
        query = "select * from RANDOMPOST"
        cursor.execute(query)
        rv = cursor.fetchall()
        #print(rv)
        payload = []
        content = {}
        for result in rv:
            content = {'id': result[0], 'first': result[1], 'second': result[2],'creation_date':result[3]}
            payload.append(content)
            content = {}
        return jsonify(payload)

    if request.method == 'POST':
        req = request.get_json()
        first = req['first']
        second = req['second']
        query = "INSERT into `RANDOMPOST`(`first`,`second`) values('" +first+ "','" +second+ "')"
        #print("query: "+query)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(query)
        res = conn.commit()
        return jsonify({'ok':'ok'})

if __name__ == '__main__':
    app.run(debug=True)