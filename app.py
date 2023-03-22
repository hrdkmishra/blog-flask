from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from models.posts import posts
from secret import SECRET_KEY

app = Flask(__name__)

# '777a8e3e7f7b33e356669e1a2668a3d6'
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='Abouts')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login')


if __name__ == '__main__':
    app.run(debug=True)
