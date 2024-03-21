import setuptools

with open("README.md", "r", encoding="utf-8") as fhand:
    long_description = fhand.read()

setuptools.setup(
    name="primefaclearner-cli",
    version="0.0.1",
    author="Mythendros & lunatics",
    author_email="amogus@web.de",
    description=("An Cli-Tool to help you memorize prime factorisations "
                "demonstrate python module and tool packaging."),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mythendros/primefaclearner",
    project_urls={
        "Bug Tracker": "",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "primefaclearner = primefaclearner.cli:main",
        ]
    }
)   
