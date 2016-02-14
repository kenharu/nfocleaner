from codecs import register_error

import click
import nfocleaner.nfocleaner as n

register_error('replace_with_space', n.replace_with_space)

@click.command()
@click.option('-o', '--out', default='-', type=click.File('w'),\
              help='Output file. Defaults to stdout.')
# Read input by replacing non-ascii characters with spaces.
@click.argument('nfo', type=click.File(encoding='ascii',\
                                       errors='replace_with_space'))
def clean(nfo, out):
    lines = nfo.read().splitlines()
    stripped = n.list_strip([l.rstrip(' ') for l in lines])
    print(*n.deindent(stripped), sep='\n', file=out)
