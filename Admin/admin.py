from flask import Flask, render_template

app = Flask(__name__)

@app.route('/admin')
def admin():
    return render_template('index.html')

@app.route('/admin/pedidos')
def admin_pedido():
    return render_template('general.html')

if __name__ == '__main__':
    app.run(port = 3000, debug = True)  