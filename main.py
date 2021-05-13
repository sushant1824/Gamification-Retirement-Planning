
# importing Flask and other modules 
from flask import Flask, request, render_template,redirect ,url_for
from flask_mysqldb import MySQL
# Flask constructor 
from flask import flash
app = Flask(__name__)    
app.config["CACHE_TYPE"] = "null"
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'game'
app.static_folder = 'static'
mysql = MySQL(app)
app.secret_key = "super secret key"

#with app.app_context():
 #  cursor = mysql.connection.cursor()
  
# A decorator used to tell the application 
# which URL is associated function 

Age=0
retirement_Age=0
@app.route('/register',methods =["GET", "POST"])
def register():
   if request.method == "POST":
      name=request.form["name"]
      email=request.form["email"]
      password=request.form["password"]
      insert_stmt = ("INSERT INTO register(Username,Email,Password,Retypepassword,UserId)" "VALUES (%s,%s,%s,%s,%s)")
      data = (name,email,password,password,name)
      cursor = mysql.connection.cursor()
      cursor.execute(insert_stmt,data)
      mysql.connection.commit()
      cursor.close()
      return redirect(url_for('login'))   
   return render_template("register.html")


@app.route('/login',methods =["GET", "POST"])
def login():
   if request.method == "POST":
      name=request.form["user"]
      #email=request.form["email"]
      password=request.form["password"]
      return render_template("Home.html")
   return render_template("login.html")


@app.route('/gamification', methods =["GET", "POST"])
def gamification():
   if request.method == "POST":  
      # getting input with name = fname in HTML form 
      amount=[]
      amount.append( request.form["equity"])
      amount.append(request.form["bond"])
      amount.append(request.form["gold"])
      amount.append(request.form["mutualfund"] )
      ctc=100
      saving=30
      #cursor = mysql.connection.cursor()
      #query_string = "SELECT bond,equity,mutualfund,gold FROM user_data WHERE Year= %s"
      ##cursor.execute(query_string,(2025))
      #mysql.connection.commit()
      #cursor.close()
      #amount=cursor.fetchall()
      y=0
      z=[]
      for x in amount:
         y=y+int(x)
      z.append(y)   
      #cursor.execute(''' SELECT bond,equity,mutualfund,gold, FROM USER_TOTAL WHERE User_Id=Id''')
      #i=0
      #for row in cursor.fetchall():
      #  amount_rec+=(row+100.0)/100.0*(amount[i]+100.0)/100.0*ctc*saving/100     
      #   i=i+1
      ##i=0
      #for row in cursor.fetchall():
      #   amount_tot+=(row+100.0)/100.0*((amount[i]+100.0)/100.0*ctc*saving/100+total[i])
      #   i=i+1     
      
      # getting input with name = lname in HTML form  
      #last_name = request.form.get("lname")
      #flash(y)
      flash('Thank you for registering: %s',y)
      #return redirect('/gamification')  
      #return redirect(url_for('success'))  

   return render_template("Gamification_Form.html")



@app.route('/', methods =["GET", "POST"]) 
def main_page(): 
   if request.args.get('type')=='register': 
      return redirect(url_for('register')) 
   if request.args.get('type')=='home':  
      return render_template("Home.html") 
   return render_template("Home.html") 
  
if __name__=='__main__': 
   app.run(debug=True) 
