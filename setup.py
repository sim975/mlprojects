from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """Reads the requirements file and returns a list of requirements."""
    requirements = []
    
    with open(file_path, "r") as file_obj:  # ✅ Fix: Use file_path variable correctly
        requirements = file_obj.readlines()  # ✅ Fix: Use readlines() properly
        requirements = [req.strip() for req in requirements]  # ✅ Remove newlines
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)  # ✅ Remove editable install if present
    
    return requirements

setup(
    name="mlproject",
    version="0.1",
    author="Simran",
    author_email="drsimran69@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
