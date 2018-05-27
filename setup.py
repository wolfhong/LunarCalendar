from setuptools import setup
from os import path


def read(fname):
    """Loads the contents of a file, returning it as a string"""
    return open(path.join(path.dirname(__file__), fname)).read()


setup(
    name='LunarCalendar',
    version='0.0.1',
    description='A lunar calendar converter, contains a number of solar holidays and lunar holidays, mainly from China.',
    long_description=read("README.rst"),
    author='wolfhong',
    author_email='hongxucai1991@gmail.com',
    url='https://github.com/wolfhong/LunarCaendar',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
    keywords=[
        'Lunar Caendar', 'festival', 'Chinese festivals',
    ],
    license='MIT',
    packages=["lunarcalendar"],
    install_requires=[
        'python-dateutil>=2.7.2',
    ],
    python_requires='>=2.7, <4',
    entry_points={
        'console_scripts': [
            'lunar-find = lunarcalendar.command:find',
            'lunar-convert = lunarcalendar.command:convert'
        ],
    },
)
