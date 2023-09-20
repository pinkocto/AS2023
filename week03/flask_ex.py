from flask import Flask
from flask import request
# html/css는 프론트엔드라고 생각 & 플라스크는 백엔드!

app = Flask(__name__)

@app.route("/")
def first_page(): # 첫페이지에 나올 값 화면에 구구단페이지 출력. (이부분을 길게해서 템플릿으로 따로 뺄 것.)
    return """
    <!DOCTYPE html>
<html lang="kr">
<head>
    <meta charset="UTF-8">
    <title>Flask Home Page</title>
</head>
<body>
    <form method="GET", action="http://127.0.0.1:5000/gugu">
        <h2>구구단 출력하기</h2>
        <label>단:
            <input type="text" name="dan">
        </label>
        <button type="submit">출력</button>
    </form>
</body>
</html>
    
    """

@app.route("/hello")
def hello_world():
    return "<a href='/'>첫 페이지</a> <a href='/hello'>Hello</a><p>Hello, World!</p>"

@app.route("/gugu") # parameter를 받을 수 있음.
def gugudan(): # dan을 빼고
    dan = int(request.args.get('dan'))
    # dan = int(dan)
    resp = ""
    resp += "<html>\n"
    resp += "<body>\n"
    resp += f"<h2>구구단 {dan}단</h2>\n"
    resp += "<div>\n"
    for i in range(1, 20):
        resp += f"{dan:2d} * {i:2d} = {dan * i:3d}<br>\n"  # d는 int를 의미. / 소수는 f
    resp += "</div>\n"
    resp += "</body>\n"
    resp += "</html>\n"
    
    
    #return "<a href='/'>첫 페이지</a> <a href='/hello'>Hello</a><p>Hello, World!</p>"
    #return f"구구단 {dan}단"
    return resp

app.run(host="0.0.0.0")
