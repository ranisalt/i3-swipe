from setuptools import setup


setup(
    name='i3-swipe',
    py_modules=['i3-swipe'],
    install_requires=['pyi3'],
    entry_points={
        'console_scripts': [
            'i3-swipe = i3-swipe:run',
        ],
    },
)
