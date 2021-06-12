# html 로 응답 지시
from flask import Flask, render_template

app = Flask(__name__)

from flask import request
# post & get 방식 적용
# post 방식 test
@app.route('/', methods=['post','get'])
def index():
    print('요청 방식 확인 -----', request.method)
    # html page 실행 즉 렌더링 지시
    # templates 하위의 html 파일 실행시 templates 폴더명은 절대 코드에 적용 하지 않음
    return render_template('step02response.html')

if __name__ == '__main__':
    app.run(debug=True)
