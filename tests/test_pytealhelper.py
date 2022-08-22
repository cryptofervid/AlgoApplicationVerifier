from githubrepo import GithubCodeRepository
from pytealhelper import PyTealHelper


def test_extract_code():

    expected_value = """
    #pragma version 2
    byte "reserve"
    byte "reserve"
    app_global_get
    int 0
    byte "balance"
    app_local_get
    +
    app_global_put
    int 1
    return
    """

    pytealgithub = GithubCodeRepository('https://github.com/algorand/pyteal/blob/master/examples/application/asset.py')
    pytealhelper = PyTealHelper(pytealgithub.get_raw_code(), 'approval_program', pytealgithub.get_raw_code(), 'clear_state_program', 2)
    print(pytealhelper.get_approval_teal())

    assert