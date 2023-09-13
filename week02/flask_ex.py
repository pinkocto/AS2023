from flask import Flask

app = Flask(__name__)

@app.route("/")
def first_page():
    return "<a href='/'>첫 페이지</a> <a href='/hello'>Hello</a><p>첫페이지 입니다.</p>"

@app.route("/hello")
def hello_world():
    return "<a href='/'>첫 페이지</a> <a href='/hello'>Hello</a><p>Hello, World!</p>"

@app.route("/gugu/<dan>") # parameter를 받을 수 있음.
def gugudan(dan):
    dan = int(dan)
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
