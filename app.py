from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
pg_user = 'postgres'
pg_pwd = '1596'
pg_port = '5432'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://{username}:{password}@localhost:{port}/computer-db".format(username=pg_user, password=pg_pwd, port=pg_port)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)

class Computer(db.Model):

    __tablename__ = "computers"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    memory_in_gb = db.Column(db.Integer)


    def __init__(self, name, memory_in_gb):
        self.name = name
        self.memory_in_gb = memory_in_gb

    def __repr__(self):
        return f"This {self.name} has {self.memory_in_gb} GB of memory"

class Company(db.Model):

    __tablename__ = "Companies"
    company_id = db.Column(db.Integer, primary_key = True)
    company_name = db.Column(db.Text)
    location = db.Column(db.Text)

    def __init__(self, company_name, location):
        self.company_name = company_name
        self.location = location


class User(db.Model):

    __tablename__ = "Users"
    user_id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.Text)
    company_id = db.Column(db.Integer, db.ForeignKey(Company.company_id))
    joining_date = db.Column(db.Text)


    def __init__(self, user_name, company_id, joining_date):
        self.user_name = user_name
        self.company_id = company_id
        self.joining_date = joining_date


@app.route('/')
def show_all():
    return render_template('show.html',users = User.query.all())


@app.route('/new', methods=['POST'])
def new():
    if request.method=='POST':
        if not request.form['user_name'] or not request.form['company_id'] or not request.form['Joining date']:
            flash('Please enter all the fields', 'error')
        else:
            new_user = User(request.form['user_name'], request.form['company_id'], request.form['Joining date'])
            db.session.add(new_user)
            db.session.commit()
            flash('Record was added successfully')
            return redirect(url_for('show_all'))
    return render_template('new.html')


@app.route('/delete', methods=['POST'])
def delete():
    if request.method=='POST':
        x = User.query.get(request.form['user_id'])
        db.session.delete(x)
        db.session.commit()
        return redirect(url_for('show_all'))
    return


if __name__ == '__main__':
    app.run(debug=True)