import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="AB_tests", BIG_HOSH
    version="0.0.1",
    author="Ayodeji-imanuel",
    author_email="emmanuelayodeji09@gmail.com",
    description="sequential, Classic and ML a/b testing",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url="https://github.com/hoshai/AB-HypothesisTesting",
    packages=setuptools.find_packages(),
    classifiers=[
        "programming Language :: python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_require='>=3.6',
)
