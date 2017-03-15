"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, flash
from models import UserProfile
from forms import UserForm
import time, os
from werkzeug.utils import secure_filename

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')
    
@app.route('/profile', methods=["POST", "GET"])
def profile():
    form = UserForm()
    
    if request.method == 'POST':
        filefolder = app.config['UPLOAD_FOLDER']
        try:
            # Get validated data from form
            uid = str(request.form['lastname']) + str(request.form['firstname']) + str(request.form['age'])
            fname = request.form['firstname'] 
            lname = request.form['lastname']
            gender = request.form['gender']
            age = request.form['age']
            usr= request.form['username']
            bio = request.form['bio']
            
            dp = request.files['dp']
            
            
            date = time.strftime("%m/%d/%Y")
            
            dpname= secure_filename(dp.filename)
            dst = filefolder + dpname
             
            
            # save user to database
            user = UserProfile(user_id =uid, first_name=fname, last_name=lname, username=usr, age=age, gender=gender, bio=bio, dp= dst, date_created=date)

            db.session.add(user)
            db.session.commit()
            
            
            dp.save(os.path.join(filefolder,dpname))

            flash('User successfully added', 'success')
            next = request.args.get('next')
            return render_template('home.html')
        except:
            flash("Unsuccessful. Try again.", 'danger')
            return render_template('profile.html', form=form)
    else:
        return render_template('profile.html', form=form)
        
@app.route("/profiles", methods=["GET", "POST"])
def profiles():
    if request.method == "GET":
        user = UserProfile.query.all()

    return render_template("profiles.html", users= user)
    
@app.route("/profile/<userid>", methods=["GET","POST"])
def userProfile(userid):
    if request.method=="GET":
        user = UserProfile.query.filter_by(user_id=userid).first()
        if user is not None:
            return render_template('profiles.html', users = user)


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    i = 0
    app.run(debug=True,host="0.0.0.0",port="8080")
