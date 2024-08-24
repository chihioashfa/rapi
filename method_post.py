from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/method_post', methods=['GET', 'POST']) #sub 페이지 구성
def method_post():
	return render_template('method_post.html')

#sub페이지를 새로 만드는건 아니고 연결<form method="post" action="/method_post_act">
@app.route('/method_post_act', methods=['GET', 'POST']) 
def method_get_act():
	if request.method == 'POST':
		id = request.form["id"] #form에서 name이 id인 input 값을 받는것
		password = request.form["password"] #form에서 name이 password인 input 값을 받는것
		return render_template('method_post.html', id=id, password=password)
		#html을 반환하는게 아니고 id와 password만 반환해서 h2에서 받는다

if __name__ == '__main__':
	app.run(debug=True, port=80, host='0.0.0.0')