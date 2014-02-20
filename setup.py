from distutils.core import setup

MAIN_PKG = 'lala'


##################
# Read pkg_info
##################

import json
from os.path import join
with open(join(MAIN_PKG, 'pkg_info.json')) as fp:
    _info = json.load(fp)


##################

setup(
        name=MAIN_PKG,
        version=_info['version'],
        author='Andrew Lee',
        packages=[MAIN_PKG],
        #license='LICENSE.txt',
        long_description=open('README.md').read(),
        install_requires=['numpy >= 1.6.0'],
        )
