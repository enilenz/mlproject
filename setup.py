from setuptools import find_packages, setup
from typing import List

HYPEN_EDOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_EDOT in requirements:
            requirements.remove(HYPEN_EDOT)
        
    return requirements



setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Eniayo',
    author_email = 'eni.odubawo@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)