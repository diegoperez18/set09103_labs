from flask import Flask, render_template, request, make_response

app = Flask(__name__)

# Product catalog (for demonstration purposes)
products = [
    {'id': 1, 'name': 'Product 1', 'price': 10.99},
    {'id': 2, 'name': 'Product 2', 'price': 19.99},
    {'id': 3, 'name': 'Product 3', 'price': 5.99},
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
            # Get the current basket or create a new one
            basket = request.cookies.get('basket', '{}')
            basket = eval(basket)

            # Add the selected product to the basket
            if str(product_id) in basket:
                basket[str(product_id)] += 1
            else:
                basket[str(product_id)] = 1

            # Save the updated basket in a cookie
            resp = make_response(render_template('index.html', products=products))
            resp.set_cookie('basket', str(basket))


           return resp
  
if __name__ == '__main__':
app.run(host='0.0.0.0', debug=True)

                                                                            
