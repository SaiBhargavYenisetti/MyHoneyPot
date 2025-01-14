import datetime

def log_connection(addr):
    with open("logs/honeypot_log.txt", "a") as log_file:
        log_message = f"{datetime.datetime.now()} - Connection from {addr}\n"
        log_file.write(log_message)
        print(log_message)
