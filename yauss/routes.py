from flask import (Blueprint,
                   render_template,
                   request,
                   redirect,
                   current_app as app)

url_crud = Blueprint('url_crud', __name__, template_folder='templates')

@url_crud.route('/', methods=['POST'])
def handle_create_url():
    app.api.create_url(request.form['long_url'])
    return redirect('/')

@url_crud.route('/<key>')
@app.cache.cached()
def handle_read_url(key):
    url = app.api.read_url_or_404(key)
    return redirect("http://" +  url['long_url'])

@url_crud.route('/update/<key>', methods=['POST'])
def handle_update_url(key):
    print(request.form['long_url'])
    app.api.update_url(key, request.form['long_url'])
    return redirect('/')

@url_crud.route('/delete/<key>')
def handle_delete_url(key):
    app.api.delete_url(key)
    return redirect('/')

@url_crud.route('/update/<key>', methods=['GET'])
def show_update_view(key):
    url = app.api.read_url_or_404(key)
    return render_template('update.html', url=url)

@url_crud.route('/', methods=['GET'])
def show_index_view():
    urls = app.api.read_all_urls()
    return render_template('index.html', urls=urls)
