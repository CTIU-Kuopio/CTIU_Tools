from setuptools import setup, find_packages

setup(
    name="filesorter",
    version="0.0.1",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.13.11",
    install_requires=[
    ],
)
