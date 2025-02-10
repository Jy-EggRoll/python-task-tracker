import datetime

def get_datetime():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_time

if __name__ == "__main__":
    get_datetime()