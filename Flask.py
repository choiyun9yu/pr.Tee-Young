from flask import Flask
from flask import render_template
# 랜더 템플릿은 현재 실행되고 있는 파일과 같은 경로에 있는 templates 폴더 내 HTML문서를 불러오는 모듈

app=Flask(__name__)

@app.route('/', methods=['GET', "POST"])
def main():
    return render_template(['main.html'])

app.run(debug=True)