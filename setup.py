from setuptools import setup, find_packages

setup(name='IBM_DEPENDENCIES',
        version='1.00',
        description="",
        packages=find_packages(),
        keywords='Bluegroup',
        author='ManuelIBM',
        author_email='juan.manuel.ruiz.plascencia@ibm.com',
        license="Apache License, Version 2.0",
        url='https://github.com/ThomasIBM/ibmBluegroup',
        include_package_data=True,
        zip_safe=False,
        install_requires=[
            'httplib2',
        ],
)