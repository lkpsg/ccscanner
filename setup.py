import setuptools

with open("README_pip.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="ccscanner",
    version="0.0.1",
    author="",
    author_email="",
    description="A SBOM scanner for C/C++",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages = setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points = {
        'console_scripts': [
            'ccscanner_print = ccscanner.scanner:main',
        ]
    }
)