from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = 'BHAVIKA JETWANI' 
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name = SRC_REPO,
    version = '0.0.1',
    author = AUTHOR_NAME,
    author_email = 'bhavika.j.2502@gmail.com',
    description = 'A package used to create the web app for movie recommender system',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    package = [SRC_REPO],
    python_requirements = '>=3.7',
    install_requirements = LIST_OF_REQUIREMENTS,

)