from flask import (Flask, 
                   render_template,
                   request,
                   redirect)

from models import db, Url, Key, with_scoped_session
from keys import consume_key


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///..\\instance\\test.db'
db.app = app
db.init_app(app)

@app.route('/<my_key>')
def my_redirect(my_key):
    url_to_redirect = Url.query.get_or_404(my_key)
    return redirect("http://" + url_to_redirect.long_url)

@app.route('/delete/<my_key>')
def handle_delete_url(my_key):
    delete_url(my_key)
    return redirect('/')

@app.route('/update/<my_key>', methods=['GET'])
def show_update_view(my_key):
    url = Url.query.get_or_404(my_key)
    return render_template('update.html', url=url)
        

@app.route('/update/<my_key>', methods=['POST'])
def handle_update_url(my_key):
    update_url(my_key, request.form['long_url'])
    return redirect('/')

@app.route('/', methods=['GET'])
def show_index_view():
    urls = Url.query.order_by(Url.date_created).all()
    return render_template('index.html', urls=urls)

@app.route('/', methods=['POST'])
def handle_add_url():
    add_url(request.form['long_url'])
    return redirect('/')

@with_scoped_session
def delete_url(my_key, session=None):
    url = session.query(Url).get_or_404(my_key)
    session.delete(url)

@with_scoped_session
def update_url(my_key, long_url, session=None):
    url = session.query(Url).get_or_404(my_key)
    url.long_url = long_url

@with_scoped_session
def add_url(long_url, key_string=None, session=None):
    if key_string is None:
        new_key = consume_key(session)
    else:
        new_key = Key(my_key=key_string, used=True)
        session.add(new_key)

    new_url = Url(my_key=new_key.my_key, long_url=long_url)
    session.add(new_url)

if __name__ == "__main__":
    app.run(host='localhost', port='5000')