from setuptools import setup, find_packages

setup(
    name="llm_batch_processor",
    version="0.1.2",
    author="Karthik Ravichandran",
    author_email="tkgravikarthik@gmail.com",
    description="A package to process CSV text data in batches using OpenAI API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/llm_batch_processor",
    packages=find_packages(),
    install_requires=[
        "openai",
        "pandas",
        "python-dotenv",
        "tqdm"
    ],
    entry_points={
        "console_scripts": [
            "llm-process=scripts.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
