from algosdk import v2client
import os


class AlgoTealHelper:
    def __init__(self, application_id: int):
        self.application_id = application_id
        self.approval = ""
        self.clear = ""

    def download_teal_bytecode(self) -> None:
        algo_d = v2client.algod.AlgodClient(algod_token="", algod_address=os.getenv("algod_url"))
        application = algo_d.application_info(self.application_id)
        self.approval = application['params']['approval-program']
        self.clear = application['params']['clear-state-program']

    def teal_to_bytecode(self, teal_code: str) -> str:
        algo_d = v2client.algod.AlgodClient(algod_token="", algod_address=os.getenv("algod_url"))
        teal_bytecode = algo_d.compile(teal_code)
        return teal_bytecode['result']
