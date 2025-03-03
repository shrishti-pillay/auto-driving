from setuptools import setup, find_packages

setup(
    name="my_project",
    version="0.1",
    packages=find_packages(where="src"),
    install_requires=[
        "pytest==8.3.4"
    ],
    package_dir={"": "src"},
)