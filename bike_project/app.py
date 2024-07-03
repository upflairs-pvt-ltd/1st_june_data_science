from flask import Flask,render_template,url_for,request

app = Flask(__name__)

@app.route('/')  
def home():
    return render_template('index.html')


@app.route('/prediction',methods=['GET','POST'])
def prediction():
    if request.method == "POST":
        brand = int(request.form['brand_name'])
        owner = int(request.form['owner'] )
        kms_driven = int(request.form['kms_driven'] )
        age = int(request.form['age'] )
        power = int(request.form['power'] )



        unseen_data = [[owner,brand,kms_driven,age,power]]    # x_variables 


  
        return unseen_data




if __name__ == "__main__":
    app.run(debug=True)
