import setuptools

with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name="pycentreon",
    version="0.1",
    author="Cyril Marcot",
    author_email="cyril.marcot@gmail.com",
    description="A SDK for python to communicate with Centreon",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cyrilmarcot/PyCentreon",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "wheel",
        "requests"
    ]
)
