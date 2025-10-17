from setuptools import setup, find_packages

setup(
  name='ekispertapi_sdk_comm',
  version='0.6.1',
  packages=find_packages(),
  install_requires=[
    # 依存パッケージをここに列挙
    'requests',
  ],
  include_package_data=True,
  author='Atsushi Nakatsugawa',
  author_email='atsushi@moongift.co.jp',
  description='SDK for Ekispert API Community Edition',
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
