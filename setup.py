from setuptools import setup

# Work around mbcs bug in distutils.
# http://bugs.python.org/issue10945
import codecs
try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')
    func = lambda name, enc=ascii: {True: enc}.get(name=='mbcs')
    codecs.register(func)

setup(
    name='nfocleaner',
    description='Remove art from NFO files.',
    author='kenharu',
    version='0.1',
    install_requires=['click'],
    tests_require=['nose'],
    test_suite='nose.collector',
    license='MIT',
    packages=['nfocleaner'],
    entry_points={
        'console_scripts': ['nfocleaner=nfocleaner.command_line:clean'],
    },
    zip_safe=True
)
