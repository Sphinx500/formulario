import web 
import app 

render=web.template.render('application/views/personas/')

class Delete():

    def GET(self):
      try:
        return render.delete()
      except Exception as e:
        return "Error" + str(e.args)
