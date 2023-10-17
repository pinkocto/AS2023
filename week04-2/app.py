from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def first_page():
    return render_template("index.html")

@app.route("/about")
def about_me_func():
    return render_template("about_me.html")

@app.route("/blog_list")
def blog_list_func():
    datasets = [
        {"title": "제목1", "content": "제목1의 내용"},
        {"title": "제목2", "content": "제목2의 내용"},
        {"title": "제목3", "content": "제목3의 내용"},
        {"title": "제목4", "content": "제목4의 내용"}
    ]
    # return render_template("blog_list.html", posts = datasets)
    return render_template("blog_list.html", posts=datasets[::-1])

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)