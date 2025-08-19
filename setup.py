from setuptools import setup, find_packages

setup(
  name='ekispert',
  version='0.5.0',
  packages=find_packages(),
  install_requires=[
    # 依存パッケージをここに列挙
    'requests',
  ],
  include_package_data=True,
  entry_points={
    'console_scripts': [
      'my_command=my_package.module:main_function',
    ],
  },
  author='Atsushi Nakatsugawa',
  author_email='atsushi@moongift.co.jp',
  description='SDK for Ekispert API',
  long_description=open('README.md').read(),
  long_description_content_type='text/markdown',
  url='https://github.com/EkispertMania/python_sdk',
  classifiers=[
      'Programming Language :: Python :: 3',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
  ],
  python_requires='>=3.6',
)
