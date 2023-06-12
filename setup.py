from distutils.core import setup
REQUIRES = [
    'grpc',
    'grpcio'
    'structlog'
    ]

setup(
    name='dm_api_search',
    version='0.0.2',
    packages=['dm_api_search'],
    url='https://github.com/surovp/dm_api_search.git',
    license='MIT',
    author='Pavel Surov',
    author_email='-',
    install_requires=REQUIRES,
    description='API clients gen'
)
