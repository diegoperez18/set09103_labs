from flask import Flask, render_template

app = Flask(__name__)

basket = []

@app.route('/')
def root():
    total_price = sum([price for _, price in basket])
    return render_template('index.html', basket=basket, total_price=total_price)

@app.route('/add_to_basket/<item>/<float:price>', methods=['POST'])
def add_to_basket(item, price):
    basket.append((item, price))
    total_price = sum([price for _, price in basket])
    return render_template('index.html', basket=basket, total_price=total_price)

@app.route('/remove_from_basket/<item>', methods=['POST'], endpoint='remove_from_basket')
def remove_from_basket(item):
    for i, (basket_item, _) in enumerate(basket):
        if basket_item == item:
            del basket[i]
            break
    total_price = sum([price for _, price in basket])
    return render_template('index.html', basket=basket or [], total_price=total_price)

@app.route('/fruits', endpoint='fruits')
def fruits():

    return render_template('fruits.html')

@app.route('/drinks', endpoint='drinks')
def drinks():
   
   return render_template('drinks.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

                                                                            
