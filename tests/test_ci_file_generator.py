"""File generator for CI pipeline specs on different CI server system vendors"""

class PipeGenerator:
    def __init__(self):
        self._ci_vendor = None

    def set_ci_vendor(self,ci_vendor=None):
        if ci_vendor == "gha":
            self._ci_vendor = "github actions"

    def using_vendor(self):
        return self._ci_vendor

def test_sut_should_allow_set_a_ci_vendor():
    """Generator should both set and comunicate what ci vendor will be used"""
    sut = PipeGenerator()
    sut.set_ci_vendor(ci_vendor="gha")
    assert sut.using_vendor()=="github actions"
