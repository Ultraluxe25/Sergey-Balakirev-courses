from flask import Flask, render_template

app = Flask(__name__)
menu = ['Installation', 'First launch', 'Feedback']


@app.route('/')
def index():
    return render_template('index.html', menu=menu)


@app.route('/about')
def about():
    return render_template('about.html', title='About the Site', menu=menu)


if __name__ == '__main__':
    app.run()
