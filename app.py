from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

basket = []
total_price = 0

@app.route('/')
def root():
    
    return render_template('index.html')

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
    return render_template('fresh.html', basket=basket, total_price=total_price)

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
    return render_template('cart.html', basket=basket, total_price=total_price)


@app.route('/fresh', endpoint='fresh')
def fresh():

    return render_template('fresh.html')

@app.route('/delivery', endpoint='delivery')
def delivery():

   return render_template('delivery.html')

@app.route('/forms', endpoint='forms')
def forms():

    return render_template('forms.html')

@app.route('/submit_membership', methods=['POST'])
def submit_membership():

    return redirect(url_for('cart'))


@app.route('/cart', endpoint='cart')
def cart():

    total_price = sum([item_dict['price'] * item_dict['quantity'] for item_dict in basket])
    return render_template('cart.html', basket=basket, total_price=total_price)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

                                                                            
