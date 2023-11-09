from flask import Flask, render_template

app = Flask(__name__)

basket = []

@app.route('/')
def root():    
    return render_template('index.html', basket=basket)

@app.route('/add_to_basket/<item>', methods=['POST'])
def add_to_basket(item):
    basket.append(item)
    return render_template('index.html', basket=basket)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

                                                                            
