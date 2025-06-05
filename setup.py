from setuptools import setup, find_packages


setup(
    name='ppack',  
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
    ],
    author='HYOJIN JO',
    description='A lightweight biosignal preprocessing package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/hynn0254/ppack',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)
