
import setuptools

with open('README.md', encoding='utf-8') as file:
    readme = file.read()

setuptools.setup(
    name='logging-config',
    version='0.1.2',
    description='Simple logging done right',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/dorinclisu/logging-config',
    author='Dorin Clisu',
    author_email='dorin.clisu@gmail.com',
    license='MIT',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    python_requires='>=3.5',
    install_requires=['colorlog']
)
