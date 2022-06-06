from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    
fav_countries = ['Japan','India','Myanmar','Nepal','France']
    return render_template('index.html', fav_countries=fav_countries)

    @app.route('/test')
    def test():
        return 'i love to travel'