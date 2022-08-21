from algohelper import AlgoTealHelper
from githubrepo import GithubCodeRepository


def test_download_bytecode_downloads_code():
    coderepo = GithubCodeRepository(
        'https://github.com/tinymanorg/tinyman-contracts-v1/blob/main/contracts/validator_approval.teal')
    code = coderepo.get_raw_code()

    algo_teal_helper = AlgoTealHelper(552635992)
    algo_teal_helper.download_teal_bytecode()
    generated_bytecode = algo_teal_helper.teal_to_bytecode(code)
    print(generated_bytecode)

    if generated_bytecode == algo_teal_helper.approval:
        print("Verified code with commit-id: " + coderepo.commit_id)
    else:
        print("Not verified")
