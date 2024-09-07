import pytest
import unittest.mock
import sys

notebookutils = unittest.mock.Mock()
sys.modules["notebookutils"] = notebookutils

import src.source_code

mock_exists = unittest.mock.Mock()
mock_exists.return_value = True

@unittest.mock.patch("notebookutils.fs.exists", new=mock_exists)
def test_some_function():
    assert src.source_code.some_function("/some/path") is True