import web 
import app 

render=web.template.render('application/views/')

class Formulario():

    def GET(self):
      try:
        return render.formulario()
      except Exception as e:
        return "Error" + str(e.args)
