from flask import Flask, render_template

app = Flask(__name__)

# Ana sayfa route'u
@app.route('/')
def home():
    return render_template('index.html')

# Giriş sayfası route'u
@app.route('/login')
def login():
    return render_template('login.html')  # login.html şablonunu döndürür

# Kayıt sayfası route'u
@app.route('/register')
def register():
    return render_template('register.html')  # register.html şablonunu döndürür

if __name__ == '__main__':
    app.run(debug=True)