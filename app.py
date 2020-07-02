import web

urls = (
    '/', 'application.controllers.fields.Formulario',
    '/delete', 'application.controllers.delete.Delete',
    '/insert', 'application.controllers.insert.Insert',
    '/list', 'application.controllers.list.List',
    '/update', 'application.controllers.update.Update',
    '/view', 'application.controllers.view.View',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()