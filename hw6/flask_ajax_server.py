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
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <script
            src="https://code.jquery.com/jquery-3.7.1.min.js"
            integrity="sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo="
            crossorigin="anonymous"></script>
    <title>Document</title>
</head>
<body>
    <form id="form_id" action="javascript:post_query()"> # 클릭을했을때 밑의 자바스크립트 코드를 실행
        <h2>구구단 출력하기</h2>
        <label>몇 단? => </label>
        <input type="text" name="dan">
        <button type="submit">출력하기</button>
    </form>
    <div id="results"></div>

<script>
function post_query() {
    $.ajax({
        type: "GET",
        url: "http://10.55.5.125:5000/gugu",
        data: $("#form_id").serialize(),
        success: update_result,
        dataType: "html"
    });
}
function update_result(data) {
    $("#results").html(data);
}
</script>

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

    return resp

app.run(host="0.0.0.0")
