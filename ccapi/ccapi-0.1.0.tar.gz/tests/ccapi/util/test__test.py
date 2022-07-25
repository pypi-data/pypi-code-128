# imports - module imports
from ccapi._compat    import StringIO, input

# imports - test imports
from testutils import assert_input
# from testutils import mock_input, assert_input

def test_mock_input(capfd):
    query = "foobar"

    assert_input(capfd, query, "Y")
    assert_input(capfd, query, "Y", input_ = input)