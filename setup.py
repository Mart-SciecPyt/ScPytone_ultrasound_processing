from setuptools import setup, find_packages

setup(
    name="ultrasound_processing_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
        "opencv-python",
        "Pillow",
        "scipy",
    ],
    author="Tied a név",
    description="Ultrasound image processing package including masking and transformations.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Mart-SciecPyt/ScPytone_ultrasound_processing",  # Ha másik, akkor cseréld
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
