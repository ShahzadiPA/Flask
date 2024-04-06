from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return  render_template('index.html')
@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username=username, isActive =True)

@app.route('/books')
def books():
    books=[{'name':'book1','author':'MT','cover':'https://notionpress.com/blog/wp-content/uploads/2015/07/001-book-brand-cover-back-presentation-mockup-psd.jpg'}, {'name':'book2','author':'ty','cover':'https://notionpress.com/blog/wp-content/uploads/2015/07/001-book-brand-cover-back-presentation-mockup-psd.jpg'}, {'name':'book3','author':'vT','cover':'https://notionpress.com/blog/wp-content/uploads/2015/07/001-book-brand-cover-back-presentation-mockup-psd.jpg'}]
    return render_template('book.html',books=books)
app.run(debug=True)