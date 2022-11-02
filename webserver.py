from flask import Flask
  
 
app = Flask(__name__) 
  
  
@app.route('/addnumber/<int:num1>/<int:num2>') 
def add(num1,num2): 
     return f'ans is: str{num1+num2}'

@app.route('/subnumber/<int:num1>/<int:num2>') 
def sub(num1,num2): 
     return f'ans is: str{num1-num2}'
 
@app.route('/mulnumber/<int:num1>/<int:num2>') 
def mul(num1,num2): 
     return f'ans is: str{num1*num2}'

  

  
app.run()
