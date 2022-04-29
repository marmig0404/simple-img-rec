from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='simple-img-rec',
    version='0.1.1',
    description='simple template image recognition tool',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    license='MIT',
    keywords='image python template',
    author='Martin Miglio',
    url='https://github.com/marmig0404/simple-img-rec',
    download_url='https://github.com/marmig0404/simple-img-rec/releases',
    install_requires=['numpy', 'opencv-python'],
    packages=['simple_img_rec'],
    python_requires='>=3',
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'simrec = simple_img_rec.__main__:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
