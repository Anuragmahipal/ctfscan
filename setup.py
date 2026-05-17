"""Setup configuration for ctfscan"""

from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='anurag-ctfscan',
    version='1.0.0',
    description='Blazing-fast terminal utility for CTF players to find and decode flags',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Anuragmahipal',
    author_email='anuragmahipal2006@gmail.com',
    url='https://github.com/Anuragmahipal/ctfscan',
    license='MIT',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Security',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],
    entry_points={
        'console_scripts': [
            'ctfscan=ctfscan.cli:main',
        ],
    },
    keywords='ctf flag decoder security hacking capture-the-flag',
    project_urls={
        'Bug Reports': 'https://github.com/Anuragmahipal/ctfscan/issues',
        'Source': 'https://github.com/Anuragmahipal/ctfscan',
    },
)
