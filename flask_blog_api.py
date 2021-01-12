from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Babita Kumari',
        'title': 'Flask Post 1',
        'content': 'First post content',
        'date_posted' : 'Jannuary 7, 2021'
    },
    {
        'author': 'Anand Krishna',
        'title': 'Flask Post 2',
        'content': 'Second post content',
        'date_posted' : 'Jannuary 10, 2021'
    }
]

@app.route("/")
@app.route("/hello")
def hello():
    return "<h1>Hello Page</h1>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"


# @app.route("/home")
# def home():
#     return '''
#     <!doctype html>
#     
#     
#     <html>
#     
#     '''


@app.route("/homeHtml")
def homeHtml():
    return  render_template('home.html', posts=posts)

@app.route("/aboutHtml")
def aboutHtml():
    return  render_template('about.html',title='AboutHtml')



if __name__ == '__main__':
    app.run(debug=True)



