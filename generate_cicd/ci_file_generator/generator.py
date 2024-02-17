"""Ci file generator for x ci vendor"""

class PipeGenerator:
    """Resp: To present use cases"""
    def __init__(self):
        self._ci_vendor = None

    def set_ci_vendor(self,ci_vendor=None):
        if ci_vendor == "gha":
            self._ci_vendor = "github actions"

    def using_vendor(self):
        return self._ci_vendor
