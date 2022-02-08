from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///dt.db"
app.config['SQLALCHEMY_DATABASE_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class paraMeter(db.Model):

    sno = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30),nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.name}"


@app.route("/",methods=['GET','POST'])

def home():
    if request.method=='POST':
        fname = request.form['fname']
        lname = request.form['lname']
        mail = request.form['mail']
        print(fname,lname,mail)
    
    user = paraMeter(name="Tushar")
    db.session.add(user)
    db.session.commit()
    allParams= paraMeter.query.all()

    return render_template('index.html',allParams=allParams)

@app.route("/about")

def about():
    return "About Us"

@app.route("/api-json")

def api():
    return app.send_static_file("dt.json")

if(__name__=="__main__"):
    app.run(debug=True, port = 8000)