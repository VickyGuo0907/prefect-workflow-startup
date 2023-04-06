from setuptools import setup, find_packages

with open("requirements.txt") as install_requires_file:
    requirements = install_requires_file.read().strip().split("\n")
setup(
    name="first-workflows",
    description="first workflow for Prefect flows",
    author="Vicky Guo",
    author_email="vicky.guo97@gmail.com",
    keywords="prefect",
    long_description_content_type="text/markdown",
    version="1.0",
    packages=find_packages(exclude=["tests"]),
    python_requires=">=3.9",
    # install_requires=requirements,
    classifiers=[
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries",
    ],
)
