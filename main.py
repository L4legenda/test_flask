from flask import Flask
from flask import request
from some_module import login
from django_module import render

app = Flask(__name__)

@app.route('/admin')
def hello_world():
    return 'admin!'

@app.route('/redirect_admin')
def hello_world():
    token_auth = request.POST['token_auth']
    url_redirect = request.POST['url_redirect'] # /admin
    
    login(token_auth)
    
    return render('<script>window.location = '{{ url_redirect }}'; </script>', # Here name html file with it content
        {"request": request, "url_redirect": url_redirect}
    )

if __name__ == '__main__':
    app.run()