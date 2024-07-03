from flask import Flask, render_template ,url_for,request
import pandas as pd 
app = Flask(__name__)

# home url "/" , url or root 
@app.route('/')
def home():
    # return "my home page "
    return render_template('home.html')

@app.route('/contact')   # http://127.0.0.1:5000/contact
def contact():
    return render_template('contact.html')


@app.route('/service')   # http://127.0.0.1:5000/service
def service():
    return render_template('service.html')

@app.route('/about')   # http://127.0.0.1:5000/about
def about():
    return render_template('about.html')


@app.route('/userdata' , methods=['GET','POST'])
def userdata():
    if request.method == 'POST':
        user_name = request.form['user_name'] 
        user_email = request.form['user_email']
        user_message = request.form['user_message']

        user_data = {'user_name':[user_name],'user_email':[user_email],
        'user_message':[user_message]}


        df = pd.DataFrame(user_data)   # single record 
        df.to_csv('user_data.csv',index=False)
        # file handling , pandas 

        return user_data 


@app.route('/quize',methods=['GET','POST'])
def quize():
    if request.method == 'POST':
        user_name = request.form['User_Name']
        return render_template('render_data.html' , user_name=user_name)



if __name__ == "__main__":
    app.run(debug=True)