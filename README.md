# Problem with mocking a library globally

## The problem

Running either of the test files independently ("pytest tests/test_file1.py" for example) is fine and creates no errors. However when running both of the tests together ("pytest"), the notebookutils mock from one file starts interfering with the imports in another file.

## Considerations

Some sources recommend using fixtures instead of patching. E.g something like this:
```
@pytest.fixture
def mock_fs_mkdirs():
    mock_mkdirs = unittest.mock.Mock(return_value=False)
    notebookutils.fs.mkdirs = mock_mkdirs

def test_other_function(mock_fs_mkdirs):
    assert src.source_code.other_function("/some/path") is False
```
which works locally, but patching notebookutils before the test is more readable and using fixtures in this way means in Fabric we would also need to mock sys.modules etc. 

It is possible to create fixtures with different [scopes](https://docs.pytest.org/en/stable/how-to/fixtures.html#scope-sharing-fixtures-across-classes-modules-packages-or-session), so I tried making a notebookutils mock fixture in the conftest.py file and set the scope to 'session' so all test files would share the same mock to avoid the interference, but unfortunately it didn't work for me.
