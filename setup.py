from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in commission_report_customized/__init__.py
from commission_report_customized import __version__ as version

setup(
	name="commission_report_customized",
	version=version,
	description="test",
	author="morteza",
	author_email="mohebi@duck.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)