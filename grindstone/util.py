import imp

def import_file(filename):
    return imp.load_source('', filename)
