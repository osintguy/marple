from setuptools import setup

setup(
   name='marple',
   version='1.0',
   description='A useful module',
   author='Man Foo',
   author_email='foomail@foo.example',
   packages=['marple'],  #same as name
   install_requires=['wheel','aiohttp','termcolor','bs4','requests','yandex_search','pypdf2','socid_extractor','maigret','aiohttp_socks','search_engines @ https://github.com/soxoj/Search-Engines-Scraper/archive/refs/heads/master.zip','tqdm','google-search-results','mock'], #external packages as dependencies
)

