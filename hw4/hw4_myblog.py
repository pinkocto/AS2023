from flask import Flask

app = Flask(__name__)

@app.route('/')
def title():
    return (
            "<nav style='color: black; background-color: yellow; font-size: 150%; text-align: center'>"
            "<a href='https://github.com/pinkocto/AS2023'>SOFTWARE</a> <a href='/TimeSeries'>TIMESERIES</a> <a href='/CodingTest'>CODING TEST</a> </nav>"
            
            "<h1> Hi there!</h1>"
            "<h3> Welcome to the page where I'm organizing and managing my study blog in 2023. </h3>"
            "<h3> I manage a blog related to time series analysis and coding tests. </h3>"
            "<h3> To access the contents about the courses and the blog links, please click on the yellow box at the top. </h3>"
            "<div style='display: flex; justify-content: center; align-items: center; height: 80vh;'>"
            "<img src = 'data:image/png;base64,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'> </div>"
    )

@app.route('/<blog_name>')
def show_detail(blog_name):
    blog_info = {
        "TimeSeries" : {"name": "2023 시계열 분석",\
                      "url": "data:image/jpeg;base64,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"},
        "CodingTest": {"name": "Coding Test Study",\
                     "url": "data:image/jpeg;base64,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"}
    }

    return  (f"<h2>{blog_info[blog_name]['name']}</h2> <hr/>"
             f"<img src='{blog_info[blog_name]['url']}'></br></br>"
             
             "<a href='/'>첫 화면으로 가기</a>")

app.run(host="0.0.0.0")
