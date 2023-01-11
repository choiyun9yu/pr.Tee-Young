from flask import Flask, request, render_template, redirect
import pymysql as ps

# 이미지 경로 적용하기
# flask app에서 static_url_path="/static" 옵션
# html에서 {{url_for('static', filename='파일명.확장자')}} 옵션 
app=Flask(__name__, static_url_path="/static")

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
    return render_template('main.html')

app.run(host='192.168.219.106',port=5031,debug=True)
