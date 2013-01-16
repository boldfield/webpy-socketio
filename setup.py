
from setuptools import setup, find_packages


setup(
    name = "webpy-socketio",
    version = "0.0.1",
    author = "Di SONG",
    author_email = "songdi19@gmail.com",
    description = ("A web.py app providing the features required to use "
                   "websockets with web.py via Socket.IO"),
    long_description = open("README.rst").read(),
    url = "https://github.com/songdi/webpy-socketio",
    py_modules=["webpy_socketio",],
    install_requires=["gevent-socketio==0.2.1", "web.py>=0.36"],
    zip_safe = False,
    include_package_data = True,
    packages = find_packages(),
    classifiers = [
        "Development Status :: 0 - Beta",
        "Environment :: Web Environment",
        "Framework :: web.py",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
    ]
)
