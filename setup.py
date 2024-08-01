from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="strct-tool",
    version="0.4.5",
    author="Salah alhajj",
    author_email="contact@contact.com",
    description="A tool for creating project structures from templates",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/salah-alhajj/strct",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "strct=strct.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "strct": ["templates/*"],
    },
)