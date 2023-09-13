from rich import print


def main():
    dan = 7
    print("<html>")
    print("<body>")
    print(f"<h2>구구단 {dan}단</h2>")
    print("<div>")
    for i in range(1, 20):
        print(f"{dan:2d} * {i:2d} = {dan * i:3d}<br>") # d는 int를 의미. / 소수는 f
    print("</div>")
    print("</body>")
    print("</html>")

if __name__ == "__main__":
    main()
