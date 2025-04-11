from setuptools import setup, find_packages

setup(
    name="ai-box-container",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "docker", 
    ],
    entry_points={
        "console_scripts": [
            "ai-box-container=ai_box_container.main:main",
        ],
    },
    author="jiahao",
    author_email="lj-hao@foxmail.com",
    description="A tool to pull and run AI application on Seeed AI Box.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ai-box-container",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
