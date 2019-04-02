import time
import psutil
from flask import Flask
from flask import render_template


app = Flask(__name__)

def displayMB():
    old_value = 0    

    while True:
        new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

        if old_value:
            send_stat(new_value - old_value)

        old_value = new_value

        time.sleep(1)

def convert_to_mbit(value):
    return value/1024./1024.*8

def send_stat(value):
    return ("%0.3f MB" % convert_to_mbit(value))
    
@app.route('/')
def hello_world(name=None):
    return "12"

if __name__ == "__main__":

    app.run(host='127.0.0.1', port='5000')