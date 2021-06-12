'''
동일한 url로 방식만 구분해서 개발 가능


'''



from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/', methods=['post'])
def post():
    print('요청 방식 확인 -----', request.method)
    return render_template('step03response.html')

@app.route('/', methods=['get'])
def get():
    print('요청 방식 확인 -----', request.method)
    return render_template('step03response.html')



if __name__ == '__main__':
    app.run(debug=True)
