import os.path
from setuptools import setup, find_packages


def read_file(fn):
    with open(os.path.join(os.path.dirname(__file__), fn)) as f:
        return f.read()

setup(
    name="skeleton",
    version="0.0.1",
    description="skeleton",
    long_description=read_file("README.md"),
    author="jang",
    author_email="",
    license="Apache License 2.0"

    packages=find_packages(),

    entry_points={
        'console_scripts': [
            'cmd = skeleton.cmd:main',
        ],
    },

    install_requires=[
                      "argcomplete",
                     ],
    tests_require=[
                    "pytest",
                    "flake8",
                  ],
)
