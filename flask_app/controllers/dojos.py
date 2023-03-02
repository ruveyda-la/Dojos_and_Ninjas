from flask_app.models.dojo import Dojo
from flask_app import app,render_template, request, redirect

@app.route("/dojos")
def read_all():
    dojos = Dojo.get_all()
    return render_template("read_all.html", dojos=dojos)

@app.route("/dojos/<int:id>")
def read_one_with_ninjas(id):
    data={'id':id}
    dojo= Dojo.get_one_with_ninjas(data)
    return render_template('read_one.html',dojo=dojo)


@app.route("/dojos/new",methods=['POST'])
def create_dojo():
    Dojo.save_dojo(request.form)
    print(request.form)
    return redirect("/dojos")












            
