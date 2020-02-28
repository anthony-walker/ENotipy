import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Notipy", # Replace with your own username
    version="0.0.1",
    author="Anthony Walker",
    author_email="dev.notipy@gmail.com",
    description="Notipy is a package to wrap your code and email you upon it's completion",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/awa1k3r/Notipy",
    entry_points={
        'console_scripts': [
            'notipy=notipy.notipy:lineRun'
        ]
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
