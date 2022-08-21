from pyteal import *

class PyTealHelper:
    def __init__(self, approval_code: str, approval_method: str, clear_state_code: str, clear_state_method: str, teal_version: int):
        self.approval_code = approval_code
        self.approval_method = approval_method
        self.clear_state_code = clear_state_code
        self.clear_state_method = clear_state_method
        self.teal_version = teal_version


    def get_approval_teal(self):
        exec(self.approval_code, globals())
        program = globals()[self.approval_method]()
        compiled_teal = compileTeal(program, mode=Mode.Application, version=self.teal_version)

        return compiled_teal

    def get_clear_state_teal(self):
        exec(self.clear_state_code, globals())
        program = globals()[self.clear_state_method]()
        compiled_teal = compileTeal(program, mode=Mode.Application, version=self.teal_version)

        return compiled_teal







