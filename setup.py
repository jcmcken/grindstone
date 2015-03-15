from setuptools import setup
import grindstone

setup(
  name='grindstone',
  version=grindstone.__version__,
  py_modules=['grindstone'],
  install_requires=open('requirements.txt').readlines(),
)
