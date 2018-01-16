# MIT License
#
# Copyright (c) 2018 Zalan Borsos
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import numpy as np
from setuptools import Extension
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize('segment_tree.pyx'),
    include_dirs=[np.get_include()]
)

from setuptools import setup

setup(
    name='vrb',
    version='0.1',
    description='Variance Reducer Bandit',
    author='Zalan Borsos',
    author_email='zalan.borsos@inf.ethz.ch',
    license='MIT',
    keywords='machine learning online variance reduction bandits',
    install_requires=["numpy", "nose"],
    ext_modules=[Extension('vrb', sources=['segment_tree.c'], extra_compile_args=['-O3'])],
    include_dirs=[np.get_include()],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5'
    ]
)
