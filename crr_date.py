from datetime import datetime

def show_current_time():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_time}")

if __name__ == "__main__":
    show_current_time()
