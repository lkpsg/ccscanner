import os
import json
import argparse

import logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger()

from ccscanner.extractors.cmake_extractor import CmakeExtractor




class scanner(object):
    def __init__(self, dir_target) -> None:
        self.target = dir_target
        self.deps = []
        self.scan()

    def scan(self):
        for root, dirs, filenames in os.walk(self.target):
            for filename in filenames:
                extractor = None
                if filename == 'CMakeLists.txt' or filename.endswith('.cmake'):
                    extractor = CmakeExtractor
                    arg = os.path.join(root, filename)

                if extractor is None:
                    continue
                try:
                    extractor = extractor(arg)
                    extractor.run_extractor()
                    res = extractor.to_dict()
                    self.deps += res['deps'] + res['libs']
                except Exception as e:
                    logger.error(e)
                    
    # def to_dict(self):
    #     return json.loads(json.dumps(self, default=lambda o: o.__dict__))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, help='Directory to scan')
    args = parser.parse_args()
    scanner_obj = scanner(args.dir)
    print(scanner_obj.deps)

if __name__ == '__main__':
    main()