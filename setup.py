from setuptools import find_packages, setup

import sparksql_magic

setup(
    name='sparksql-magic',
    version=sparksql_magic.__version__,
    description='Spark SQL magic command for Jupyter notebooks',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    author='Chaerim Yeo',
    author_email='yeochaerim@gmail.com',
    url='https://github.com/cryeo/sparksql-magic',
    license='MIT License',
    install_requires=['pyspark>=2.3.0', 'ipython>=7.4.0'],
    packages=find_packages(exclude=('tests', 'docs')),
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
