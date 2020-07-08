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
            print(form)
            print(form.id)
            print(form.nombre)
            print(form.pri_ap)
            print(form.seg_ap)
            print(form.age)
            print(form.date)
            print(form.gender)
            print(form.state)
            return render.insert()
        except Exception as e:
            return "Ups, algo salio mal"