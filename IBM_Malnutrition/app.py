from flask import Flask, render_template, request,session

app = Flask(__name__)
app.secret_key ='a'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/severewasting')
def swasting():
    return render_template('severewasting.html')

@app.route('/overweight')
def overweight():
    return render_template('overweight.html')

@app.route('/underweight')
def underweight():
    return render_template('underweight.html')
@app.route('/stunting')
def stunting():
    return render_template('stunting.html')
@app.route('/wasting')
def wasting():
    return render_template('wasting.html')


# @app.route('/register', methods=['POST','GET'])
# def register():
#     if request.method == "POST":
#         name = request.form['name']
#         email = request.form['email']
#         contact = request.form['mobile']
#         address = request.form['address']
#         role = request.form['role']
#         if role =="0":
#             role = "Faculty"
#         else:
#             role = "Student"
#         branch = request.form['branch']
#         password = request.form['pwd']
        
#         #inp=[name,email,contact,address,role,branch,password]
#         insertdb(conn,name,email,contact,address,role,branch,password)
#         return render_template('login.html')
        

# @app.route('/login', methods=['POST','GET'])
# def login():
#     if request.method == "POST":
#         email = request.form['email']
#         password = request.form['pwd']
#         sql= "select * from SB_TABLE where email='{}' and password='{}'".format(email,password)
#         stmt = ibm_db.exec_immediate(conn, sql)
#         userdetails = ibm_db.fetch_both(stmt)
#         print(userdetails)
#         if userdetails:
#             session['register'] =userdetails["EMAIL"]
#             return render_template('userprofile.html',name=userdetails["NAME"],email= userdetails["EMAIL"],contact= userdetails["CONTACT"],address=userdetails["ADDRESS"],role=userdetails["ROLL"],branch=userdetails["BRANCH"])
#         else:
#             msg = "Incorrect Email id or Password"
#             return render_template("login.html", msg=msg)
#     return render_template('login.html')


if __name__ =='__main__':
    app.run( debug = True)
