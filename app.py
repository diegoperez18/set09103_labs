from flask import Flask, render_template

app = Flask(__name__)

basket = []

@app.route('/')
def root():
    total_price = sum([item['price'] * item['quantity'] for item in basket])
    return render_template('index.html', basket=basket, total_price=total_price)

@app.route('/add_to_basket/<item>/<float:price>', methods=['POST'])
def add_to_basket(item, price):
    for item_dict in basket:
        if item_dict['item'] == item:
            item_dict['quantity'] += 1
            item_dict['total_price'] = item_dict['price'] * item_dict['quantity']
            break
    else:
        basket.append({'item': item, 'price': float(price), 'quantity': 1, 'total_price': float(price)})
    total_price = sum([item_dict['price'] * item_dict['quantity'] for item_dict in basket])
    return render_template('index.html', basket=basket, total_price=total_price)

@app.route('/remove_from_basket/<item>', methods=['POST'], endpoint='remove_from_basket')
def remove_from_basket(item):
    for item_dict in basket:
        if item_dict['item'] == item:
            if item_dict['quantity'] > 1:
                item_dict['quantity'] -= 1
                item_dict['total_price'] = item_dict['price'] * item_dict['quantity']
            else:
                basket.remove(item_dict)
            break
    total_price = sum([item_dict['price'] * item_dict['quantity'] for item_dict in basket])
    return render_template('index.html', basket=basket, total_price=total_price)


@app.route('/fruits', endpoint='fruits')
def fruits():

    return render_template('fruits.html')

@app.route('/drinks', endpoint='drinks')
def drinks():

   return render_template('drinks.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

                                                                            
