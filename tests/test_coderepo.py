from githubrepo import GithubCodeRepository


def test_getrawcode_returns_rawcode():

    expected_value = "This is a test file for testing repository code."

    coderepo = GithubCodeRepository('https://github.com/tinymanorg/tinyman-contracts-v1/blob/13acadd1a619d0fcafadd6f6c489a906bf347484/contracts/validator_approval.teal')
    #"https://raw.githubusercontent.com/sumantrana/StudentRestAPI/5b2365155f2c313d51e9cb006df1cbc6c5ecbd2f/src/test/java/com/sumant/rest/studentrest/CourseServiceTests.java"
    code = coderepo.get_raw_code()
    print(code)


