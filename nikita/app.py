from flask import Flask, render_template 
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




if __name__ == "__main__":
    app.run(debug=True)