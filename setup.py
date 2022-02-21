from setuptools import setup, find_packages

setup(
    name="files-great-expectations",
    version="0.1",
    description="Meltano project files for Great Expectations",
    packages=find_packages(),
    package_data={
        "bundle": [
            "utilities/great_expectations/README.md"
        ]
    },
)
