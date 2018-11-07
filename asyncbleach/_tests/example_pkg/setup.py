import setuptools

from asyncbleach import bleach_build_py

setuptools.setup(
    name="example_pkg",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A package used to test asyncbleach",
    url="https://github.com/pypa/sampleproject",
    packages=['example_pkg', 'example_pkg._async'],
    cmdclass={'build_py': bleach_build_py},
    package_dir={'': 'src'},
)