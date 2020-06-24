import web

urls = (
    '/', 'application.controllers.fields.Formulario',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()