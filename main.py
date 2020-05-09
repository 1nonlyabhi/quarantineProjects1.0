from flask import Flask, render_template, url_for, request, session, redirect, flash
from flask_sqlalchemy import SQLAlchemy 
from flask_mail import Mail
from werkzeug.utils import secure_filename
import json, os
from datetime import datetime
import math


# import MYSQLdb
# from flask_sqlalchemy import db
# db.create_all()


with open('E:\Python Programs\Projects\Web\config.json', 'r') as c:
    params = json.load(c)["params"]

local_server=True
app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config['UPLOAD_FOLDER'] = params['location']
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True, 
    MAIL_USERNAME = params['gmail-user'],
    MAIL_PASSWORD = params['gmail-password']
)
mail = Mail(app)

if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)
# db=MYSQLdb.connect (host ="localhost", user="root" , db="cleanpost")



class Contacts(db.Model):
    #  sno, name, email, phone_num, msg, date
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    phone_num = db.Column(db.String(12), unique=True, nullable=False)
    msg = db.Column(db.String(120), unique=False, nullable=False)
    date = db.Column(db.String(12), unique=False, nullable=False)


class Posts(db.Model):
    #  sno, title, tline, slug, content, date
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    tagline = db.Column(db.String(80), unique=False, nullable=False)
    slug = db.Column(db.String(21), unique=True, nullable=False)
    content = db.Column(db.String(120), unique=False, nullable=False)
    img_file = db.Column(db.String(12), unique=False, nullable=False)
    date = db.Column(db.String(12), unique=False, nullable=False)
    writer = db.Column(db.String(21), unique=False, nullable=False)

@app.route('/')
def home():
    posts = Posts.query.filter_by().all() # [0:params['no_of_posts']]
    last = math.ceil(len(posts)/int(params['no_of_posts']))
    page = request.args.get('page')
    if(not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page-1)*int(params['no_of_posts']): (page-1)*int(params['no_of_posts']) + int(params['no_of_posts'])]
    if(page == 1):
        prev = "#"
        next = "/?page=" + str(page+1)
    elif(page == last):
        prev = "/?page=" + str(page-1)
        next = "#"
    else:
        prev = "/?page=" + str(page-1)
        next = "/?page=" + str(page+1)
    return render_template('index.html', params = params, posts=posts, prev = prev, next = next)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
    if ('user' in session and session['user'] == params['admin_user']):
        posts = Posts.query.all()
        return render_template('dashboard.html', params=params, posts=posts)

    if request.method=='POST':
        admin_username = request.form.get('uname')
        admin_password = request.form.get('pass')
        if (admin_username == params['admin_user'] and admin_password == params['admin_pass']):
            session['user'] = admin_username
            posts = Posts.query.all()
            return render_template('dashboard.html', params=params, posts=posts) 

    return render_template('login.html', params=params)

@app.route('/uploader', methods=['GET','POST'])    
def uploader():
    if ('user' in session and session['user'] == params['admin_user']):
        if(request.method == 'POST'):
            file = request.files['file']
            if file:
                file.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
                flash(f'File Uploaded successfully at {datetime.now()}')
                return redirect (url_for('dashboard'))
            flash('Please select the file first !')
        return redirect (url_for('dashboard'))
            

@app.route('/edit/<string:sno>', methods=['GET', 'POST'])
def edit(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == 'POST':
            title = request.form.get('title')
            tagline = request.form.get('tline')
            slug = request.form.get('slug')
            content = request.form.get('content')
            img_file = request.form.get('img_file')
            writer = request.form.get('writer')
            date = datetime.now()

            if sno == '0':
                post = Posts(title=title, slug=slug, content=content, tagline=tagline, img_file=img_file, writer=writer, date=date)
                db.session.add(post)
                db.session.commit()
            else:
                post = Posts.query.filter_by(sno=sno).first()
                post.title = title
                post.tagline = tagline
                post.slug = slug
                post.content = content
                post.img_file = img_file
                post.writer = writer
                post.date = date
                db.session.commit()
                return redirect('/edit/'+sno)
        post = Posts.query.filter_by(sno=sno).first()
        return render_template('edit.html', params = params, post=post, sno=sno)

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    if(request.method== 'POST'):
        # fetch entry from page
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        # add entry to database
        entry = Contacts(name=name, email=email, phone_num=phone, msg=message, date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New Msg from' + name, 
                            sender=email, 
                            racipients = [params['gmail-user']],
                            body=message + "\n" + phone
                            )
    return render_template('contact.html')

@app.route('/post/<string:post_slug>', methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug = post_slug).first()
    return render_template('post.html', params = params, post = post)

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('dashboard')

@app.route('/delete/<string:sno>', methods=['GET', 'POST'])
def delete(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        post = Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('dashboard')

app.run(debug=True)
