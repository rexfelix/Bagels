import entrypoints
from setuptools import setup, find_packages

with open("README.md", "r") as fn:
    long_description = fn.read()

setup(
    entry_points={
        "console_scripts": ["bagels=bagels.cmd.bagels_cmd:bagels_play", ]
    },
    name="bagel",
    version="0.0.1",
    author="Rexfelix",
    author_email="rexfelix@naver.com",
    description="세 자리 숫자 맞추기 게임",
    long_description=long_description,
    url="https://github.com/rexfelix/python_example",
    include_dirs=[],
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Development Status::4-Beta",
        "Programming Language::Python::3",
        "Operating System::OS Independent",
    ],
    requires=[],

)
