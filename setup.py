from setuptools import setup

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
