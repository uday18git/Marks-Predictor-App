# setup.py will be responsible in creating my ml application as a package and we can install this package in your projects also and you can use it we can also deploy in pypi and any body can use it.
from setuptools import setup, find_packages,setup
from typing import List
HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    #this function will return the list of requirements
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements
setup(
    name='mlproject',
    version='0.0.1',
    author = 'Uday',
    author_email = 'kcuday07@gmail.com',
    packages = find_packages(),#finds all the __init__.py files and creates a package
    install_requires = get_requirements('requirements.txt')
)