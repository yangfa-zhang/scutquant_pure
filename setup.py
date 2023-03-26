from setuptools import setup, find_packages

setup(
    name='scutquant',
    version='0.3.2',
    packages=find_packages(),
    install_requires=[
        'numpy >= 1.21.6',
        'pandas >= 1.1.5',
        'matplotlib >= 3.4.1',
        'xgboost >= 1.6.2',
        'lightgbm >= 3.3.0',
        'seaborn >= 0.11.2',
        'scipy >= 1.7.1',
        'statsmodels >= 0.13.0'
    ],
    author='ChanHarley',
    author_email='2434722850@qq.com',
    description='A quantitative investment platform designed by SCUTQTA',
    url='https://github.com/chn489/scutquant_pure',
    project_urls={
        'Source Code': 'https://github.com/chn489/scutquant_pure'
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    license='MIT',
    keywords='example package',
)