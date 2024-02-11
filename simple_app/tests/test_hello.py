from ..app import App

def test_system_should_say_hello():
    app = App()
    assert app.say_hello() == "hello!"
