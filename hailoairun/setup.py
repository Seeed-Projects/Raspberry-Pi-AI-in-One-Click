from setuptools import setup, find_packages

setup(
    name="hailoairun",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "docker>=6.0.0",
    ],
    entry_points={
        "console_scripts": [
            "hailoairun=hailoairun.cli:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool to pull and run Hailo AI applications",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/hailoairun",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 