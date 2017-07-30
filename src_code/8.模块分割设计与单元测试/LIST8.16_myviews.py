def index():
    s = SomeService()
    result = s.some_method(**self.request.params)
    request.environ['render_context'] =  dict(result=result)
    return render('index.html', self.render_context)
