"""App unitesting for tdd"""
from ..app import App
import pytest

def test_system_should_say_hello():
    """System should say hello to user"""
    app = App()
    assert app.say_hello() == "hello!"

@pytest.mark.integration
def test_integration_test():
    assert True
