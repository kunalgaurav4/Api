from flask import Flask, render_template, request
from form import RegisterForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'kunal.123'
app.config['RECAPTCHA_USE_SSL']= False
app.config['RECAPTCHA_PUBLIC_KEY']= '6LdWzL0UAAAAAM7GiksDy92_U_RmMHzvK2oFHatI'
app.config['RECAPTCHA_PRIVATE_KEY']='6LdWzL0UAAAAAK3sFKsA8x835Bsds9-jr6ZhoXMP'
app.config['RECAPTCHA_OPTIONS'] = {'theme':'white'}

@app.route('/')
def index():
    title = "Homepage"
    
    return render_template("index.html")

@app.route('/register.html', methods=['GET', 'POST']) 
def register(): 
    form = RegisterForm()

    if form.validate_on_submit():
            return "the form has been submitted. Success!"

    return render_template("register.html", form=form)

if __name__ == '__main__':
    app.run(port=5000, debug=True)  