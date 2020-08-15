from flask import Flask, render_template
from flask_mysqldb import MySQL
import pyodbc  
import pypyodbc

app = Flask(__name__)

mysql = MySQL()
 
# MySQL configurations
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'password123'
#app.config['MYSQL_DB'] = 'test'
#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
#mysql = MySQL(app)

#MS SQL Server
#connection = pypyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:vrajdb.database.windows.net,1433;Database=vrajdb;Uid=virgil;Pwd=azure@123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
connection = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=tcp:vrajdb.database.windows.net;'
                      'Database=vrajdb;'
                      'Uid=virgil;'
                      'Pwd=azure@123;'
                      'TrustServerCertificate=no;'
                      )


#define basic route
@app.route("/")
def main():
    #cur = mysql.connection.cursor()
    ##cur = connection.cursor()
    #cur.execute('''select * from mytable ''')
    #res = cur.fetchall()
    #print(res)
    return render_template('index.html'

if __name__ == "__main__":
    app.run()