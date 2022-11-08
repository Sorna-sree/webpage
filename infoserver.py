from flask import Flask, render_template 
  
app = Flask(__name__) 
  
  
@app.route('/page') 
def python(): 
     return render_template('form.html') 
    
@app.route('/form') 
def details(): 
     detail = [ 
         {"salutation":"Mr","firstName":"S. ","lastName":"Kannan","phoneNo":65743,"Occupation":"HR"}, 
         {"salutation":"Ms","firstName":"S. ","lastName":"Sornasree","phoneNo":34567,"Occupation":"Engineer"}, 
         {"salutation":"Dr","firstName":"K. ","lastName":"senthamilkumaran","phoneNo":89076,"Occupation":"Manager"}, 
         {"salutation":"Mrs","firstName":"S. ","lastName":"Riyaswari","phoneNo":67579,"Occupation":"teacher"}
         
         ] 
     return detail
  
app.run(host='0.0.0.0')
