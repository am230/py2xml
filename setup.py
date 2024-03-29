from setuptools import setup, find_packages, find_namespace_packages

with open('README.rst', mode='r', encoding='utf-8') as f:
    long_description = f.read()

author = 'am230'
name = 'py2xml'
py_modules = [name]

setup(
    name=name,
    version="1.0.5",
    keywords=("javascript", "convert", "translator"),
    description="Write XML with Pythonic Code",
    long_description=long_description,
    requires=["strbuilder"],
    license="MIT Licence",
    long_description_content_type='text/x-rst',
    packages=find_packages(),
    url=f"https://github.com/{author}/{name}",
    author=author,
    author_email="am.230@outlook.jp",
    py_modules=py_modules,
    platforms="any",
)