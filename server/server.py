from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

from passwordGen import genPassword
 
# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)

#Allows server to be hosted externally
app.run(host='0.0.0.0')
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

app.jinja_env.globals.update(genPassword=genPassword)
 
class ReusableForm(Form):
    hooli = TextField('New Hooli Password:', validators=[validators.required(), validators.EqualTo('Hooliv', message='Hooli Passwords must match')])
    piper = TextField('New Pied Piper Password:', validators=[validators.required(), validators.EqualTo('Piperv', message='Pied Piper Passwords must match')])
    myspace = TextField('New Myspace Password:', validators=[validators.required(), validators.EqualTo('MyspaceV', message='Myspace Passwords must match')])
 
    def reset(self):
        blankData = MultiDict([ ('csrf', self.reset_csrf() ) ])
        self.process(blankData)
 
 
@app.route("/", methods=['GET', 'POST'])
def form():
    form = ReusableForm(request.form)

    print form.errors
    if request.method == 'POST':
        name=request.form['name']
        print name
 
        if form.validate():
            # Save the comment here.
            flash('Hello ' + name)
        else:
            flash('All the form fields are required. ')
 
    return render_template('password.html', form=form, p1=genPassword(), p2=genPassword(), p3=genPassword())
 
if __name__ == "__main__":
    app.run()