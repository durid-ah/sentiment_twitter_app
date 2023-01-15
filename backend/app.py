from flask import Flask
import pymssql

app = Flask(__name__)

server = 'mssqldb'
database = 'sentiment_app'
username = 'sa'
password = 'DevPassword1'


@app.route('/')
def hello_world():
   return 'Hello, Docker!'

@app.route('/data')
def get_data():
   conn = pymssql.connect(server=server, user=username, password=password)
   cursor = conn.cursor()# as_dict=True)

   cursor.execute('SELECT @@version')
   print('DURID...')
   for row in cursor:
      print(row)

   conn.close()

   return 'yay'