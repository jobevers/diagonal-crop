import setuptools


setuptools.setup(
    name = "diagonal-crop",
    version = "1.0.0",
    packages = setuptools.find_packages(exclude=['tests']),
    install_requires=['pillow>=3.1.1'],
    setup_requires=['nose>=1.0'],
    tests_require=['mock>=2.0.0']
)
