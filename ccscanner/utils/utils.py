import json
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)


def read_txt(txt):
    try:
        with open(txt, 'r', errors='ignore') as load_f:
            content = load_f.read()
    except:
        try:
            with open(txt, 'r', encoding='latin-1') as load_f:
                content = load_f.read()
        except:
            logger.error('File read error occurred: ', txt)
            return None
    return content


# remove substring from left
def remove_lstrip(s, substring):
    if not s.startswith(substring):
        return s
    else:
        return s[len(substring):]


# remove substring from right
def remove_rstrip(s, substring):
    if not s.endswith(substring):
        return s
    else:
        return s[:len(substring)*-1]