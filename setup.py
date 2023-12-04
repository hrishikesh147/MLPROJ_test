from setuptools import setup,find_packages

NAME="MLPROJECT TEST"
VERSION="0.0.0.1"
DESC="ML Proj test"
AUTHOR="hrishikesh bhagawati"
AUTHOR_EMAIL="hrishikeshbhagawati@gmail.com"

req="requirements.txt"
HYPHEN_E_DOT="-e ."

def get_requirements():
    with open(req,'r') as req_file:
        req_file=req_file.readlines()

        req_list=[i.replace("\n","") for i in req_file]
        if HYPHEN_E_DOT in req_list:
            req_list.remove(HYPHEN_E_DOT)
    return req_list


setup(
   name='foo',
   version='1.0',
   description='A useful module',
   author='Man Foo',
   author_email='foomail@foo.example',
   packages=find_packages(),
   install_requires=get_requirements()
)