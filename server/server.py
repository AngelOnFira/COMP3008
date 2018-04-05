from flask import Flask, render_template, request, make_response
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from passwordGen import genPassword
import random, string

users = {}

# App config.
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

def getUID():
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))

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
    
    thisUser = {
        "p1":genPassword(),
        "p2":genPassword(),
        "p3":genPassword()
    }

    uid = getUID()
    
 
    response = make_response(render_template('password.html', form=form, thisUser['p1'], thisUser['p2'], thisUser['p3']))
    response.set_cookie('uid', getUID())
    return response

if __name__ == "__main__":
    app.run()