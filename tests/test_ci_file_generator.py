"""File generator for CI pipeline specs on different CI server system vendors"""

def test_sut_should_allow_set_a_ci_vendor():
    """Generator should both set and comunicate what ci vendor will be used"""
    sut = PipeGenerator()
    sut.set_ci_vendor(ci_vendor="gha")
    assert sut.using_vendor()=="github actions"


