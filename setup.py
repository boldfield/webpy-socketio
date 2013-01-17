
from setuptools import setup, find_packages

required = (
    #"gevent-socketio",
    "web.py>=0.36"
)


setup(
    name="webpy-socketio",
    version="0.0.2",
    author="Di SONG, Brian Oldfield",
    author_email="songdi19@gmail.com, brian@oldfield.io",
    description=("A web.py app providing the features required to use websockets with web.py via Socket.IO"),
    long_description=open("README.rst").read(),
    url="https://github.com/boldfield/webpy-socketio",
    py_modules=["webpy_socketio", ],
    install_requires=required,
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
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
