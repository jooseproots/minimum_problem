import notebookutils

def some_function(path):
    return notebookutils.fs.exists(path)

def other_function(path):
    return notebookutils.fs.mkdirs(path)