from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "7332735770:AAG99jxzmWsdBQxQsDV8nLTnCyG1nUY-uKg"
USER_ID = "7331003037"

@app.route('/signal', methods=['POST'])
def signal():
    data = request.get_json()
    pair = data.get('pair')
    entry = data.get('entry')
    tp1 = data.get('tp1')
    tp2 = data.get('tp2')
    sl = data.get('sl')

    message = f"""🚨 New Signal Alert
📊 Pair: {pair}
📈 Entry: {entry}
🎯 TP1: {tp1}
🎯 TP2: {tp2}
🛑 Stop Loss: {sl}"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={'chat_id': USER_ID, 'text': message})

    return "Signal sent!"

app.run(host='0.0.0.0', port=5000)