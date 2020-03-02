from {{cookiecutter.project_name}} import hello

def test_say_hello():
    app = hello.HelloWorld()
    assert None == app.say_hello(name='John')
