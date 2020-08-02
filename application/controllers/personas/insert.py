import web 
import app 

render=web.template.render('application/views/personas/')

class Insert():

    def GET(self):
      try:
        return render.insert()
      except Exception as e:
        return "Error" + str(e.args)

    def POST(self):
        try:
            form = web.input()
            id=form.id
            nombre= form.nombre
            primer_apellido=form.pri_ap
            segundo_apellido=form.seg_ap
            edad= form.age
            fecha_nac=form.date
            genero=form.gender
            Estado=form.state
            render.insert(nombre,pri_ap,seg_ap,age,date,gender,state)
            web.seeother('/list')
        except Exception as e:
            print("Ups, algo salio mal")
            return render.insert()
            