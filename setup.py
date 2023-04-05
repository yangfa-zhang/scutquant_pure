from setuptools import setup, find_packages

setup(
    name='scutquant',
    url='https://github.com/HaoningChen/scutquant',
    author='HarleyChan',
    license='MIT',
    version='0.4.2',
    packages=find_packages(),
    install_requires=[
        'numpy >= 1.21.6',
        'pandas >= 1.1.5',
        'sklearn >= 0.0.post1'
        'matplotlib >= 3.4.1',
        'xgboost >= 1.6.2',
        'lightgbm >= 3.3.0',
        'seaborn >= 0.11.2',
        'scipy >= 1.7.1',
        'statsmodels >= 0.13.0'
        'keras >= 2.6.0',
        'tensorflow >= 2.3.4',
        'akshare >= 1.9.29'
    ],
)