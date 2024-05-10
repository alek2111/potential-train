from flask import Flask, request, render_template, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'product_name' in request.form:
            product_name = request.form['product_name']
            send_to_telegram(product_name)
            return redirect(url_for('index'))

        else:
            return 'No product name provided'
    return render_template('111.html')

def send_to_telegram(product_name):
    bot_token = 'TOKEN'
    chat_id = 'ID'
    message = f' {product_name}'
    requests.get(f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}')

if __name__ == '__main__':
    app.run(debug=True)