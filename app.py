from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/about')
def harry():
    name = 'Kshitij'
    return render_template('about.html', name = name)
if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
