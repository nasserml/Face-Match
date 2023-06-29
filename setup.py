from setuptools import setup

setup(
    name='src',
    version='0.0.1',
    author='nasserml',
    description='a small package for To Whom does your face match',
    author_email='nassermanone@gmail.com',
    packages=['src'],
    python_requires='>3.7',
    install_requires=['mtcnn',
                    'tensorflow==2.3.1',
                    'PyYAML',
                    'tqdm',
                    'scikit-learn',
                    'streamlit',
                    'bing-image-downloader']
)