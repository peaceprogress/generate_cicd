"""Ci file generator for x ci vendor"""

class PipeGenerator:
    """Resp: To present use cases"""
    def __init__(self,pipe_specs=None):
        self._vendor = None
        self._load_specs(pipe_specs)

    def set_ci_vendor(self,ci_vendor=None):
        if ci_vendor == "gha":
            self._vendor = "github actions"

    def using_vendor(self):
        return self._vendor

    def _load_specs(self,pipe_specs=None):
        """load specs for generate pipeline files"""
        self._vendor = pipe_specs.get_vendor()
        self._vcs_vendor = pipe_specs.get_vcs_vendor()
        self._stages = pipe_specs.get_stages()
        self._platform = pipe_specs.get_platform()

    def using_vcs_vendor(self):
        return self._vcs_vendor
    
    def using_platform(self):
        return self._platform

    def adding_stages(self):
        return self._stages
