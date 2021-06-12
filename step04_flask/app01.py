from flask import Flask

# flask 객체(instance) 생성
app = Flask(__name__)



# url 설정 - http://ip:port/ 또는 http://ip:port 형식으로 구성
# @ : 장식자
@app.route('/playdata')
def index():
    return '{"name":"유재석"}'

if __name__ == '__main__':

    app.run(debug=True)