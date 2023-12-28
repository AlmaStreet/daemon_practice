from setuptools import setup, find_packages

# Read the contents of your requirements.txt file
with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="DaemonKit",
    version="0.1",
    packages=find_packages(),
    install_requires=required,
    entry_points={
        "console_scripts": [],
    },
    author="Jason Chen",
    author_email="jason.jia.chen@gmail.com",
    description="A powerful toolkit for seamless daemon process creation and management in Python.",
    long_description=open("README.md").read(),
    url="https://github.com/AlmaStreet/daemonkit",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
