from setuptools import setup, find_packages

setup(name='IBM_BlueUtilities',
        version='1.1',
        description="This Package help to management of bluegroups and retrieve basic information from bluepages.",
        packages=find_packages(),
        keywords='Bluegroup,BluePages',
        author='Manuel_Ruiz',
        author_email='juan.manuel.ruiz.plascencia@ibm.com',
        license="Apache License, Version 2.0",
        url='https://github.com/ManuelRuiz39/IBM_DEPENDENCIES',
        include_package_data=True,
        zip_safe=False,
        install_requires=[
            'requests',
        ],
)