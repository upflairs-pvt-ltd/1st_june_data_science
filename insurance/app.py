from flask import Flask,render_template,url_for,request
app = Flask(__name__)

@app.route('/')  # url 
def home():
    return render_template('home.html')


@app.route('/project')  # http://127.0.0.1:5000/project
def project():
    return render_template('project.html')


@app.route('/predict',methods=['GET','POST']) # http://127.0.0.1:5000/predict
def predict():
    if request.method == "POST":
        # to recieve the data 
        region = request.form['region']
        children = request.form['children']
        health = request.form['health']
        smoker = request.form['smoker']
        gender = request.form['gender']
        bmi = request.form['bmi']
        age = request.form['age']
        unseen_data = [region,children,health,smoker,gender,bmi,age]
        return unseen_data




if __name__ == "__main__":
    app.run(debug=True)