from string import printable
from itertools import dropwhile
from codecs import replace_errors, register_error

def replace_with_space(exception):
    """
    Implement the 'replace_with_space' error handling (for text encodings only):
    substitute encoding/decoding errors with an ascii space.
    """
    _, pos = replace_errors(exception)
    return (' ', pos)

def count_leading_character(s, char=' '):
    """Count the leading occurrences of 'char' in the string 's'."""
    return len(s) - len(s.lstrip(char))

def deindent(lines):
    """Remove superflous indentation."""
    non_empty = filter(None, lines)
    indentation = min(map(count_leading_character, non_empty))
    return [l[indentation:] for l in lines]

def list_strip(lst, el=''):
    "Return a copy of 'lst' with leading and trailing 'el's removed."
    is_el = lambda x: x == el
    return list(dropwhile(is_el, reversed(list(dropwhile(is_el, reversed(lst))))))
