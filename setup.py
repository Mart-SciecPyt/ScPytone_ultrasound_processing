from setuptools import setup, find_packages

setup(
    name="ultrasound_processing_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "opencv-python",
        "matplotlib",
        "Pillow",
        "scipy"
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A package for ultrasound image transformation and processing",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ultrasound_processing_package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
