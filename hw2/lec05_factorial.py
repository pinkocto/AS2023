def fact(num):
    result = 1
    for i in range(1, num+1):
        result = result*i
    return result

def main():
    number = 5
    print(f"{number}!은 {fact(number)}입니다.")


if __name__ == "__main__":
    main()
