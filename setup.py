from setuptools import setup, find_packages
from typing import List

requirements_lst:List[str]=[]

def get_requirements()->List[str]:

    try:
        with open("requirements.txt",'r') as f:
            lines=f.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!="-e .":
                    requirements_lst.append(requirement)
        
    except FileNotFoundError:
        print("requirements.txt file not found") 
    return requirements_lst

setup(
    name="Network_Security_Project",
    version="1.0.0",
    packages=find_packages(),
    install_requires=get_requirements(),
    author="Sunny Codex",
    author_email='sa2182780@gmail.com'
)
