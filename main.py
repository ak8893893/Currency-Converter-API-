from flask import Flask, request, jsonify

app = Flask(__name__)

# 匯率資料
exchange_rates = {
    "TWD": {
        "TWD": 1,
        "JPY": 3.669,
        "USD": 0.03281
    },
    "JPY": {
        "TWD": 0.26956,
        "JPY": 1,
        "USD": 0.00885
    },
    "USD": {
        "TWD": 30.444,
        "JPY": 111.801,
        "USD": 1
    }
}

def convert_currency(source, target, amount):
    if source not in exchange_rates or target not in exchange_rates:
        return None
    if source == target:
        return amount

    conversion_rate = exchange_rates[source][target]
    converted_amount = amount * conversion_rate
    return round(converted_amount, 2)

@app.route('/convert', methods=['GET'])
def convert():
    source = request.args.get('source')
    target = request.args.get('target')
    amount_str = request.args.get('amount')

    try:
        amount = float(amount_str.replace('$', '').replace(',', ''))
    except ValueError:
        return jsonify({"msg": "Invalid amount"}), 400

    converted_amount = convert_currency(source, target, amount)
    if converted_amount is None:
        return jsonify({"msg": "Invalid source or target currency"}), 400

    result = {"msg": "success", "amount": "${:,.2f}".format(converted_amount)}
    return jsonify(result)

if __name__ == '__main__':
    app.run()