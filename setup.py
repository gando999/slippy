try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

tests_require = ['pytest']

setup(name = "slippy",
            description="slippy - async experiment",
            long_description = """
slippy is a library for client server io experiements in Python 3.5+ 
""",
            license="""MIT""",
            version = "0.1",
            author = "Gary Anderson",
            maintainer = "Gary Anderson",
            url = "https://github.com/gando999/slippy",
            packages = ['slippy'],
            tests_require = tests_require,
            extras_require = {
                'test': tests_require,
              },
            classifiers = [
              'Programming Language :: Python :: 3',
              ]
            )
