from flask import Flask, render_template, request, Markup
from flask_ckeditor import CKEditor, CKEditorField
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'
app.config['WTF_CSRF_ENABLED'] = True
app.config['CKEDITOR_PKG_TYPE'] = 'standard'  # CKEditorのパッケージタイプを指定する（basic、standard、fullなど）
ckeditor = CKEditor(app)


class PostForm(FlaskForm):
    title = StringField('タイトル')
    content = CKEditorField('内容')
    submit = SubmitField('投稿')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if form.validate_on_submit():
        # フォームが正しく送信された場合の処理
        title = request.form.get('title')
        content = request.form.get('content')
        div = Markup(content)
        return render_template('page.html', div=div)
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
