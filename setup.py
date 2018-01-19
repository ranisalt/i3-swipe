from setuptools import find_packages, setup


setup(
    name='i3-swipe',
    packages=find_packages(),
    install_requires=['pyi3'],
    entry_points={
        'console_scripts': [
            'i3swipe = i3swipe:run',
        ],
    },
)
