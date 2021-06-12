from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('step05request.html')


@app.route('/login', methods=['post'])
def login():


    id = request.form.get('id') 
    pw = request.form.get('pw')  
    email = request.form.get('email')
    info = {'name':id, "passward":pw, "email":email }

    return render_template('step05response.html', idencore=id, userinfo=pw, mail = email) 



if __name__ == '__main__':
    app.run(debug=True)