import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="submodule",
    version="0.0.1",
    author="Sumit Lahiri",
    author_email="lahiri.devs@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codersguild/pythonista",
    project_urls={
        "Bug Tracker": "https://github.com/codersguild/pythonista/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.8",
)
