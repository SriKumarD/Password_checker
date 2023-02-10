from flask import Flask, render_template, request,redirect,jsonify,url_for
import sqlite3 
import re

app = Flask(__name__)
  
@app.route("/")  
def index():
     
    return render_template("index.html"); 
@app.route("/insert",methods = ["POST"])  
def saveDetails():
    res=[]
    username=str(request.form["username"])
    password=str(request.form["pass"])
    lc=False
    uc=False
    endnum=False
    len8=False
    if((re.search('[A-Z]', password))):
        uc=True
        res.append("")
    else:
        res.append("You did not used Uppercase character")
    if((re.search('[a-z]', password))):
        lc=True
        res.append("")
    else:
        res.append("You did not used Lowercase character")
    if((re.search('[\S]+[0-9]$', password))):
        endnum=True
        res.append("")
    else:
        res.append("You did not end your password with number")
    
    if(len(password) >= 8):
        len8=True
        res.append("")
    else:
        res.append("Your password must be atleast 8 characters")
    if(uc and lc and len8 and endnum):
        print('sai')
        try:
            with sqlite3.connect("data.db") as con:
                cur = con.cursor()  
                cur.execute("INSERT into login (username,password) values (?,?)",(username,password))
                con.commit()
                res.append('Your password passed 4 requirements:')
        except:
            res.append("Data Not Inserted Due To Connection Error")  
        finally:
            return render_template("report.html",msg=res)
    else:
        res.append('Oh no! Looks like you had issues with your password!')
        return render_template("report.html",msg=res); 
if __name__ == '__main__':
   app.run(debug = True)