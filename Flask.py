from flask import Flask
from flask import render_template
import pymysql as ps

app=Flask(__name__)

conn=ps.connect(host='localhost', user='root', passwd='1234', db='mysql')
curs=conn.cursor()
#curs=juso_db.cursor(pymysql.cursors.DictCursor)

# 한 사이클 
# sql = " "
# curs.execute(sql)
# result = curs.fetchall()
# conn.commit()
# curs.close()
# conn.close()

@app.route('/', methods=['GET', "POST"])
def main():
    return render_template(['main.html'])

app.run(debug=True)
