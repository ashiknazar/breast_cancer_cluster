from setuptools import setup,find_packages
from typing import List

hyp='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if hyp in requirements:
            requirements.remove(hyp)
    return requirements
setup(
    name='breast_cancer_cluster',
    author='AshikNazar',
    author_email='warticcotaky@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)