from datetime import datetime

def log_result(test_name, status, message=""):
    with open("results.txt", "a") as file:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{time}] {test_name} - {status}")
        
        if message:
            file.write(f" - {message}")
        
        file.write("\n")
