import pytest
import unittest.mock
import sys

notebookutils = unittest.mock.Mock()
sys.modules["notebookutils"] = notebookutils

import src.source_code

mock_mkdirs = unittest.mock.Mock()
mock_mkdirs.return_value = True

@unittest.mock.patch("notebookutils.fs.mkdirs", new=mock_mkdirs)
def test_other_function():
    assert src.source_code.other_function("/some/path") is True
