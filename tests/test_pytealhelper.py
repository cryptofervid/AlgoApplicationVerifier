from githubrepo import GithubCodeRepository
from pytealhelper import PyTealHelper


def test_extract_code():
    pytealgithub = GithubCodeRepository('https://github.com/algorand/pyteal/blob/master/examples/application/asset.py')
    pytealhelper = PyTealHelper(pytealgithub.get_raw_code(), '', '', '')
    pytealhelper.get_approval_code()