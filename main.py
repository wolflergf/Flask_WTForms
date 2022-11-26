from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In")


app = Flask(__name__)
app.secret_key = "some secret string"
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    email = "admin@email.com"
    password = "12345678"
    if form.validate_on_submit():
        if form.email.data == email and form.password.data == password:
            return redirect("success")
        else:
            return redirect("denied")
    return render_template("login.html", form=form)


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/denied")
def denied():
    return render_template("denied.html")


if __name__ == '__main__':
    app.run(debug=True)
