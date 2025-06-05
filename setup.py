from setuptools import setup, find_packages


setup(
    name='ppack',  
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        # 필요한 패키지 더 넣기
    ],
    author='your-name-or-id',
    description='A lightweight biosignal preprocessing package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/your-id/ppack',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)
