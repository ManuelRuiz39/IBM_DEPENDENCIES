from setuptools import setup, find_packages

setup(name='IBM_DEPENDENCIES',
        version='1.0',
        description="This Package help to management of bluegroups and retrieve basic information of bluepages.",
        packages=find_packages(),
        keywords='Bluegroup,BluePages',
        author='ManuelIBM',
        author_email='juan.manuel.ruiz.plascencia@ibm.com',
        license="Apache License, Version 2.0",
        url='https://github.com/ManuelRuiz39/IBM_DEPENDENCIES',
        include_package_data=True,
        zip_safe=False,
        install_requires=[
            'requests',
        ],
)