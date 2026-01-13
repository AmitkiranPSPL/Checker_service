from datetime import datetime

def main():
    with open("abcd.txt", "w", encoding="utf-8") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

if __name__ == "__main__":
    main()
