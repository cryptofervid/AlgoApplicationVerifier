from githubrepo import GithubCodeRepository


def test_getrawcode_returns_rawcode():

    expected_value = "This is a test file for testing repository code."

    coderepo = GithubCodeRepository('https://github.com/cryptofervid/AlgoApplicationVerifier/blob/main/tests/resources/test.txt')
    code = coderepo.get_raw_code()

    assert code == expected_value


