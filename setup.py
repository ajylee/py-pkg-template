from distutils.core import setup

MAIN_PKG = 'lala'

## AJL's Boiler - Load pkg_info.json from path 'p'
def _load_info(p):
    import json; from os.path import isdir, dirname
    with open((p if isdir(p) else dirname(p)) + '/pkg_info.json') as fp:
        return json.load(fp)

_info = _load_info(MAIN_PKG)

setup(
        name=MAIN_PKG,
        version=_info['version'],
        author='Andrew Lee',
        packages=[MAIN_PKG],
        #license='LICENSE.txt',
        long_description=open('README.md').read(),
        install_requires=['numpy >= 1.6.0'],
        )
