import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="abstract_event_server",
    version="0.0.1",
    author="John Janecek",
    author_email="janecektyler@gmail.com",
    description="Python server for easy overriding on post requests",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jtjanecek/AbstractEventServer",
    project_urls={
        "Bug Tracker": "https://github.com/jtjanecek/AbstractEventServer/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
	install_requires=['aiohttp', 'requests'],
	package_dir={"": "src"},
	packages=setuptools.find_packages(where='src'),
    python_requires=">=3.7",
)
