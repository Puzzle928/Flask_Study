from flask import Flask, render_template

# client가 요청시에 서버에 전송하는 데이터를 활용할 수 있는 API
from flask  import request

app = Flask(__name__)


# 첫 요청시 step04request.html로 렌더링

# get 방식
@app.route('/')
def index():
    return render_template('step04request.html')

# step04request.html 의 form tag에 입력된 데이터를 받아서 처리하는 함수
# http://127.0.0.1:5000/login
@app.route('/login', methods=['post'])
def login():

    # name속성값이 id인 tag의 value값을 획득하는 로직
    print("-----", request.form.get('id'))


    '''
     http://127.0.0.1 -> app04.py의 get방식으로 index() 실행 -> step04request.html
     -> id/pw입력 -> 로그인 버튼 클릭 (action='login' method='post' ) 
     -> url  http://127.0.0.1/login으로 id/pw를 은닉해서 post 방식으로 전송
     -> app04.py의 login url과 매핑도 login() 함수 실행
     -> 입력된 데이터값 확인 (request.form.get('id')) 이 코드로 
     -> 이동되는 다음 html에서 출력하겠금 데이터를 전송
     -> 응답하는 step04response.html에선 app04.py가 전송한 데이터값을 출력하는 기능의
     코드가 구현
    '''
    id = request.form.get('id')


    # client 가 입력한 id/pw값 획득해서 검증 로직 후에 무효? 유효? 화면으로 이동 예정
    return render_template('step04request.html', idencore= id)

if __name__ == '__main__':
    app.run(debug=True)