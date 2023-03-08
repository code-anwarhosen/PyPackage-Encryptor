from setuptools import find_packages, setup

with open("app/readme.txt", "r") as f:
    long_description = f.read()

setup(
    name="encryptor",
    version="0.0.10",
    description="This is a regular text encrypter.",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anwar-hasaan/",
    author="Anwar Hasan",
    author_email="anwarhasan202@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent (Windows[10, 11] Tested)",
    ],
    install_requires=['cryptography>=39.0.1'],
    # extras_require={
    #     "dev": ["pytest>=7.0", "twine>=4.0.2"],
    # },
    python_requires=">=3.8",
)