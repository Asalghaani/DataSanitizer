from setuptools import setup, find_packages


setup(
    name='DataSanitizer',
    version='0.1.0',
    author='Fatemeh Sadat Ghaani', 
    author_email='Asalghaani@yahoo.com',  
    description='A Python package for automatic data cleaning, handling missing values, outliers detection, and text standardization.',  
    packages=find_packages(),
    install_requires=[
        'pandas>=1.0.0',
        'numpy>=1.19.0',
        'scipy>=1.5.0',
        'scikit-learn>=0.24.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
