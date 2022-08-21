import ast
import astor
from githubrepo import GithubCodeRepository
import inspect
from pyteal import *
import parser

class PyTealHelper:
    def __init__(self, approval_code: str, approval_method: str, clear_state_code: str, clear_state_method: str):
        self.approval_code = approval_code
        self.approval_method = approval_method
        self.clear_state_code = clear_state_code
        self.clear_state_method = clear_state_method

    def get_approval_code(self):

        parser.suite(self.approval_code)

        parser.compilest()



        tree = ast.parse(self.approval_code)

        for block in tree.body:
            for node in ast.walk(block):
                if isinstance(node, ast.FunctionDef):
                    fn_name = node.name
                    if fn_name == 'approval_program':
                        fn_source = astor.to_source(node)
                        compile_obj = compile(fn_source, '', 'exec')
                        loc = {}
                        exec(compile_obj, globals(), loc)
                        print(loc['program'])
                        # compiled = compileTeal(result, mode=Mode.Application, version=2)
                        # print (compiled)


        print("Done")







