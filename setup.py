from setuptools import setup, find_packages

with open("requirements.txt") as fp:
    install_requires = fp.read()

setup(
    name="lesson1",
    version="0.0.1",
    author="Levi Muniz",
    author_email="levi.muniz17@gmail.com",
    url="https://github.com/leviem1-python-academy/lesson-1",
    description="First lesson of the leviem1 Python Academy",
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    test_suite="tests",
    install_requires=install_requires,
)
