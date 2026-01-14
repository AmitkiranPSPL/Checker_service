from datetime import datetime

def main():
    with open("abcd.txt", "w", encoding="utf-8") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    while True:
        print("Hello World One")
    return 54

if __name__ == "__main__":
    main()
