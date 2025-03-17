
from flask import Flask, render_template, request,redirect, url_for
app=Flask(__name__)

@app.route("/",methods=["GET"])
def index():
    # return "welcome to index page "
    return render_template('index.html')

@app.route("/login",methods=["GET","POST"])
def login():
    # return "welcome to index page "
    return render_template('login.html')

@app.route("/register",methods=["GET"])
def register():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        if password != confirm_password:
            return "Passwords do not match!"
        
        return redirect(url_for('login'))
    # return "welcome to index page "
    return render_template('register.html')





if __name__=="__main__":
    app.run(debug=False)
