import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="sbcommons",
    version="0.0.64",
    author="Haypp Group",
    author_email="data@hayppgroup.com",
    description="Packages shared between lambda functions and other systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Snusbolaget/lambdas",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "boto3>=1.24.35",
        "botocore>=1.27.35 ",
        "urllib3>=1.26.10",
        "requests>=2.28.1",
    ]
)
