from distutils.core import setup
import downstream

setup(
    name='downstream',
    version=downstream.__version__,
    author='Aleix Ruiz de Villa, Bartek Skorulski, Pau Rué',
    author_email='hello@downstream.cat',
    description='Seamless Causal Inference for Python',
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords="Causal Inference",
    url='http://downstream.cat',
    packages=['downstream'],
    install_requires = [
        'lark_parser==0.7.8',
        'pydot==1.4.1',
        'networkx==2.4'
    ]
 )
