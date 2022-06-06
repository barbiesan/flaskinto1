from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    user_dict = {
        'username': 'barbiesan',
        'email': 'barbiesan@gmail.com'
        }  
    colors = ['red','pink','green']
    return render_template('index.html', user=user_dict, colors=colors)

@app.route('/test')
def test():
    return 'this is a test'