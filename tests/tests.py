from methods.methods import*

def test_getRequestDocumentsIo():
    result = getRequestDocumentsIo()
    assert result.status_code == 200