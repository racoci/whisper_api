from setuptools import setup, find_packages
import pkg_resources
from pathlib import Path

setup(
    name='whisper-app',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            Path(__file__).with_name("requirements.txt").open()
        )
    ],
    author='Lucas Racoci',
    author_email='racoci.0@gmail.com',
    description='Django API for OpenAI Whisper',
    url='https://github.com/racoci/whisper_api',
)