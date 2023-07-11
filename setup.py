from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in pipedrive_erpnext/__init__.py
from pipedrive_erpnext import __version__ as version

setup(
	name="pipedrive_erpnext",
	version=version,
	description="pipedrive integration with erpnext",
	author="zubair",
	author_email="experterp771@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
