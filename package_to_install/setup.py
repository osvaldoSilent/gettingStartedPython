from setuptools import setup, find_packages

setup(
    name="packages",
    author="SilentKush",
    version=1,
    description="This is the installer for using the setup_package and setup_fileHandler locally in your python system ",
    packages=['setup_calculator','.setup_calculator', 'setup_fileHandler','.setup_fileHandler'],
    #packages= find_packages('D:\IntellijProjects\PythonProjects\installing\package_to_install\setup_package',exclude=['installer'])
)