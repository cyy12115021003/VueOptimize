from flask import Flask, render_template, request,Response,jsonifyfrom flask_cors import CORSfrom flask_script import Managerfrom datetime import datetimeAPP = Flask(    __name__,static_folder="../dist/static", template_folder="../dist")manager = Manager(APP)CORS(APP)@APP.route('/')def home():    return render_template('index.html')@APP.errorhandler(404)def page_not_found(e):    return '<h1>page is not found!</h1>'@APP.route('/test', methods=['GET','POST'])def test():    print(request.data)    time = datetime.now().strftime('%Y-%m-%d')    return time@APP.route('/user', methods=['GET','POST'])def user():    print(request.data)    return 'success!'@APP.route('/get_message', methods=['GET','POST'])def get_message():    message = { "answer":"This is a answer!" }    message = jsonify(message)    return messageif __name__ == '__main__':    APP.run(debug=True)