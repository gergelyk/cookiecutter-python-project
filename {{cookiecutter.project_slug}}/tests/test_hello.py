from {{cookiecutter.module_name}} import hello


def test_say_hello():
    app = hello.HelloWorld()
    assert None is app.say_hello(name='John')
