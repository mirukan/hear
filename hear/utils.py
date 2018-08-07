import contextlib
import sys

class DummyFile(object):
    def write(self, _):
        pass

@contextlib.contextmanager
def discard_stdout():
    real_stdout = sys.stdout
    sys.stdout  = DummyFile()
    yield
    sys.stdout = real_stdout
