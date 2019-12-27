from flask import Flask, request, render_template, send_file

application = Flask(__name__)


@application.route('/')
def my_form():
    return render_template('my-form.html')


@application.route('/user')
def user_response():
    user_name = request.args.get('user')
    return render_template('return-form.html', value=user_name)


@application.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    return render_template('return-form.html', value=text)


if __name__ == "__main__":
    application.run()

