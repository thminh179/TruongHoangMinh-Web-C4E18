from flask import Flask, render_template
app = Flask(__name__) #tao ra 1 app/server = flask

# 127.0.0.1 ~ localhost -> 127.0.0.1:5000 ~ localhost:5000
@app.route('/') # '/': dẫn đến trang chính -> trang chính hiện "Hello world"
def index():
    posts = [
        {
            "title" : "Tho Con Coc",
            "content" : "Tho",
            "author" : "Tuan Anh"
        },
        {
            "title" : "Tho Con Ech",
            "content" : "Tho Ech",
            "author" : "A"
        },
        {
            "title" : "Tho Con Voi",
            "content" : "Tho Voi",
            "author" : "B"
        }

    ]
   
    return render_template("index.html", posts = posts)


@app.route('/hello') #'/hello': route /hello
def say_hello():
    return "Hello C4E18"

@app.route('/sayhi/<name>/<age>') #<>: parameter
def say_hi(name, age):
    return "Hi {0}, you're {1} years old".format(name, age)

# @app.route('/sum/<a>/<b>') 
# def calc(a, b):
#     return str(int(a) + int(b)) #mọi parameter gửi đến server đều là string -> convert sang int rồi convert lại sang str

@app.route('/sum/<int:a>/<int:b>') #yêu cầu parameter trả ra kiểu int
def calc(a,b):
    return str(a + b)

if __name__ == '__main__': #khi file app được chạy trực tiếp 
  app.run(debug=True) 

 