import os
import shutil

import nox


def tests_impl(session):
    # Install deps and the package itself.
    session.install("-r", "test-requirements.txt")
    session.install(".")

    # Show the pip version.
    session.run("pip", "--version")
    # Print the Python version and bytesize.
    session.run("python", "--version")
    session.run("python", "-c", "import struct; print(struct.calcsize('P') * 8)")

    session.run(
        "coverage",
        "run",
        "--parallel-mode",
        "-m",
        "pytest",
        "-r",
        "sx",
        "tests",
        *session.posargs,
        env={"PYTHONWARNINGS": "always::DeprecationWarning"}
    )
    session.run("coverage", "combine")
    session.run("coverage", "report", "-m")


@nox.session(python=["2.7", "3.4", "3.5", "3.6", "3.7", "3.8", "pypy"])
def test(session):
    tests_impl(session)


@nox.session()
def blacken(session):
    """Run black code formater."""
    session.install("black")
    session.run("black", "src", "tests", "noxfile.py", "setup.py")


@nox.session
def lint(session):
    session.install("flake8", "black")
    session.run("flake8", "--version")
    session.run("black", "--version")
    session.run("black", "--check", "src", "tests", "noxfile.py", "setup.py")
    session.run("flake8", "setup.py", "docs", "src", "tests")


@nox.session
def docs(session):
    session.install("-r", "rtd-requirements.txt")
    session.install(".")

    session.chdir("docs")
    if os.path.exists("_build"):
        shutil.rmtree("_build")
    session.run("sphinx-build", "-W", ".", "_build/html")
