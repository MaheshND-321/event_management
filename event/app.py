from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
app.secret_key = "secret_key"
 
#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/event'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
 
 
#Creating model table for our CRUD database
class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    f_name = db.Column(db.String(10))
    l_name = db.Column(db.String(10))
    id_no = db.Column(db.String(10))
    email = db.Column(db.String(20))
    phone = db.Column(db.String(10))
    e_type = db.Column(db.String(20))
    e_name = db.Column(db.String(20))
    e_date = db.Column(db.Date)
    e_start_time = db.Column(db.Time)
    e_end_time = db.Column(db.Time)
 
 
    def __init__(self, f_name, l_name, id_no, email, phone, e_type, e_name, e_date, e_start_time, e_end_time):
 
        self.f_name = f_name
        self.l_name = l_name
        self.id_no = id_no
        self.email = email
        self.phone = phone
        self.e_type = e_type
        self.e_name = e_name
        self.e_date = e_date
        self.e_start_time = e_start_time
        self.e_end_time = e_end_time


#This is the index route where we are going to
#query on all our employee data
@app.route('/')
def Index():
    all_data = Data.query.all()
 
    return render_template("index.html", events = all_data)
 
#this route is for inserting data to mysql database via html forms
@app.route('/insert', methods = ['POST'])
def insert():
 
    if request.method == 'POST':
 
        f_name = request.form['f_name']
        l_name = request.form['l_name']
        id_no = request.form['id_no']
        email = request.form['email']
        phone = request.form['phone']
        e_type = request.form['e_type']
        e_name = request.form['e_name']
        e_date = request.form['e_date']
        e_start_time = request.form['e_start_time']
        e_end_time = request.form['e_end_time']
 
        my_data = Data(f_name, l_name, id_no, email, phone, e_type, e_name, e_date, e_start_time, e_end_time)
        db.session.add(my_data)
        db.session.commit()
 
        flash("Events Added Successfully")
 
        return redirect(url_for('Index'))
 
#This route is for deleting our employee
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Event Deleted Successfully")
 
    return redirect(url_for('Index'))
 
 
if __name__ == "__main__":
    app.run(debug=True)