from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
from flask_app import app,render_template, request, redirect

# @app.route("/")
# def read_all():
#     ninjas = Ninja.get_all()
#     return render_template("read_all.html", ninjas=ninjas)

# @app.route("/ninjas/<int:id>")
# def read_one(id):
#     data={'id':id}
#     ninja= Ninja.get_one(data)
#     return render_template('read_one.html',ninja=ninja)

@app.route("/ninjas")
def show_form():
    dojos=Dojo.get_all()
    return render_template("create.html",dojos=dojos)

@app.route("/ninjas/new",methods=['POST'])
def create():
    Ninja.save(request.form)
    print(request.form)
    dojo_id=request.form['dojo_id']
    return redirect(f"/dojos/{dojo_id}")


@app.route("/ninjas/edit/<int:id>")
def edit(id):
    data={'id':id}
    ninja= Ninja.get_one(data)
    return render_template('edit.html',ninja=ninja)

@app.route("/ninjas/update", methods=['POST'])
def update_ninja():
    Ninja.change_ninja(request.form)
    dojo_id=request.form['dojo_id']
    return redirect (f"/dojos/{dojo_id}")

@app.route("/ninjas/delete/<int:id>")
def delete(id):
    data={'id':id}
    ninja=Ninja.get_one(data)
    dojo_id=ninja['dojo_id']
    Ninja.delete_ninja(data)
    return redirect(f"/dojos/{dojo_id}")











            
