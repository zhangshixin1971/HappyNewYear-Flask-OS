from flask import Flask, request, render_template

application = Flask(__name__)

@application.route('/')
def my_form():
    return render_template('my-form.html')

@application.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text + " Wish you and your family Merry Christmas and Happy New Year!"
    return processed_text

if __name__ == "__main__":
    application.run()
