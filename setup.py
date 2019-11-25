from distutils.core import setup

setup(
    name='aioosuwebapi',
    packages=['aioosuwebapi'],
    version='r20191125',
    description='Asynchronous osu! api wrapper',
    author='Kyuunex',
    url='https://github.com/Kyuunex/aioosuapi',
    download_url='https://github.com/Kyuunex/aioosuapi/tarball/r20191125',
    keywords=['osu', 'api'],
    classifiers=[],
    requires=['aiohttp', 'beautifulsoup4'],
)
