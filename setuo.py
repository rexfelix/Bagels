from setuptools import setup

with open("README.md", "r") as fn:
    long_description = fn.read()

setup(
    name="bagel",
    version="0.0.1",
    author="Rexfelix",
    author_email="rexfelix@naver.com",
    description="세 자리 숫자 맞추기 게임",
    long_description="세 자리 숫자를 맞추는 게임 입니다.\n추측한 숫자가 맞지만 위치가 틀리면 'Pico',\n숫자도 맞고 자리도 맞으면 'Fermi',\n맞는 숫자가 없으면 'Bagel' "
                     "힌트를 제공 합니다. ",
    url="https://github.com/rexfelix/python_example",
    include_dirs=[],
)