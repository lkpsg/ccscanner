import sys
import os
# sys.path.append(os.getcwd())
from ccscanner.scanner import scanner

def test_scanner(target):
    scanner_obj = scanner(target)
    res = scanner_obj.deps
    return res


if __name__ == '__main__':
    target = 'tests'
    res = test_scanner(target)
    print(res)
