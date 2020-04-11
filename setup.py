import os.path
from setuptools import setup, find_packages


def read_file(fn):
    with open(os.path.join(os.path.dirname(__file__), fn)) as f:
        return f.read()

setup(
    name="skeleton",
    versioning="dev",
    setup_requires=["setupmeta"],
    packages=find_packages(exclude=["test.*, *.test", "test*"]),
)
