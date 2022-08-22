from algohelper import AlgoTealHelper


def test_download_bytecode_downloads_code():

    teal_code = """
    #pragma version 2
    int 1
    return
    """

    expected_bytecode = "AiABASJD"

    algo_teal_helper = AlgoTealHelper(552635992)
    algo_teal_helper.download_teal_bytecode()
    generated_bytecode = algo_teal_helper.teal_to_bytecode(teal_code)

    assert generated_bytecode == expected_bytecode
