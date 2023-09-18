from rich import print
# 화면에 출력되는 것을 파일로

def main():
    dan = 7

    filename = "index.html"

    with open(filename, "w", encoding="utf-8") as f:
        # 기존 기능은 안건든다.
        f.write("<html>\n")
        f.write("<body>\n")
        f.write(f"<h2>구구단 {dan}단</h2>\n")
        f.write("<div>\n")
        for i in range(1, 20):
            f.write(f"{dan:2d} * {i:2d} = {dan * i:3d}<br>\n") # d는 int를 의미. / 소수는 f
        f.write("</div>\n")
        f.write("</body>\n")
        f.write("</html>\n")

if __name__ == "__main__":
    main()
