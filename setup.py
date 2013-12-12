from setuptools import setup
import os
import distutils.sysconfig
pre = distutils.sysconfig.get_config_var("prefix")
bindir = os.path.join(pre, "bin/activate")

setup(
    name='s3_deployer',
    version='0.0.1',
    description='Deploy static directories to S3',
    author='Tim Downs',
    author_email='timothy.j.downs@gmail.com',
    zip_safe=False,
    include_package_data=True,
    url='http://tjdownsllc.com',
    platforms=["any"],
    dependency_links=[
    ],
    install_requires=[
        'fabric',
        'boto',
    ]
)
