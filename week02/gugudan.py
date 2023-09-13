from rich import print


def main():
    dan = 7
    for i in range(1, 20):
        print(f"{dan:2d} * {i:2d} = {dan * i:03d}") # d는 int를 의미. / 소수는 f

if __name__ == "__main__":
    main()
