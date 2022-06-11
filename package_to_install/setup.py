from setuptools import setup, find_packages

setup(
    name="Calculator",
    author="SilentKush",
    version=1,
    description="This is the installer for using the setup_package locally in your python system ",
    packages=['setup_package','.setup_package'],
    #packages= find_packages('D:\IntellijProjects\PythonProjects\installing\package_to_install\setup_package',exclude=['installer'])
)