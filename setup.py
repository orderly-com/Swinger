from distutils.core import setup

setup(
    name = 'Swinger',
    packages = ['Swinger'],
    package_dir={'Swinger':'Swinger'},
    package_data={'Swinger':['*.*', 'stopwords/*','dictionary/*']},
    version = '2.0',
    description = 'A sentiment classifier for Chinese',
    author = 'davidtnfsh',
    author_email = 'davidtnfsh@gmail.com',
    url = 'https://github.com/UDICatNCHU/Swinger',
    download_url = 'https://github.com/UDICatNCHU/Swinger/archive/v2.0.tar.gz',
    keywords = ['sentiment', 'sentiment analysis', 'swinger', 'chinese', 'text mining', 'udic'],
    classifiers = [],
    license='GPL3.0',
    install_requires=[
        'nltk',
        'sklearn',
        'numpy',
        'scipy',
        'jieba',
        'simplejson'
    ],
    zip_safe=True
)
