"""App unitesting for tdd"""
import pytest
from ..app import App

def test_system_should_say_hello():
    """System should say hello to user"""
    app = App()
    assert app.say_hello() == "hello!"
    assert False

@pytest.mark.integration
def test_integration_test():
    """Integration test"""
    assert True
