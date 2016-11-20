from setuptools import setup

setup(
    name="NextBus",
    packages=['Nextbus'],
    version="1.0",
    description="Fetch NextBus API data",
    author="Vlad Ionescu",
    author_email="github@vladionescu.com",
    url="https://gitlab.com/vladionescu/nextbus-python",
    install_requires=[
        "requests>=2.7.0"
    ]
)
