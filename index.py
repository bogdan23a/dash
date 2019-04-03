from flask import Flask, jsonify, render_template, request
import psutil

app = Flask(__name__)

new_value = 0
old_value = 0

def measureBandwidth():

    global new_value
    global old_value

    new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

    return new_value - old_value

@app.route('/_get_bandwidth')
def get_bandwidth():

    global old_value 
    global new_value

    old_value = request.args.get('old_value', 0, type=float) + new_value
    bandwidth = measureBandwidth()

    return jsonify(result=bandwidth)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":

    app.run(debug=True)