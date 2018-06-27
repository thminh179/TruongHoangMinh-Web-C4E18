from flask import *
import mlab
from models.service import Service
from models.customer import Customer

app = Flask(__name__)

mlab.connect()

@app.route('/')
def index():    
    return render_template('index.html')

@app.route('/search')
def search():
    all_service = Service.objects()       
    return render_template('search.html',all_service = all_service)

@app.route('/detail/<service_id>')
def detail(service_id):
    service = Service.objects().with_id(service_id)
    return render_template('detail.html', service = service )

@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template("admin.html", all_service = all_service)

# @app.route('/delete/<service_id>')
# def delete(service_id):
#     service_to_delete = Service.objects().with_id(service_id)
#     if service_to_delete is None:
#         return "Service not found"
#     else: 
#         service_to_delete.delete()
#         return redirect(url_for('admin'))

@app.route('/new', methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template("new.html")
    elif request.method == 'POST':

        form = request.form
        name = form['name']
        yob = form['yob']
        address = form['address']
        gender = form['gender']

        new = Service(
            name = name,
            yob = yob,
            address = address,
            gender = gender
        )
        new.save()
        return redirect(url_for('admin'))


if __name__ == '__main__':
    # app.run(host="127.0.0.1", port=5000, debug=True)
    app.run(debug=True)
 