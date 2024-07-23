from flask import Flask,render_template,url_for,request
import joblib 

bow_obj = joblib.load("./models/bag_of_words.lb")
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/prediction',methods=['POST','GET'])
def prediction(): 
    if request.method == "POST": 
        message = str(request.form['message'])
        email_message = [message]
        email_converted = bow_obj.transform(email_message).toarray()

        return message 





if __name__ == "__main__":
    app.run(debug=True)


