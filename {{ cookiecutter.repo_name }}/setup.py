from setuptools import find_packages, setup

setup(
    name='{{ cookiecutter.package_name }}',
    packages=find_packages(),
    version='0.1.0',
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.author_name }}',
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.package_name }} = {{ cookiecutter.package_name }}.cli:main'
        ]
    }
)
