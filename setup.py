from setuptools import setup, find_packages

setup(
    name="Data-Aggregation-Grouping-Reshaping-Analysis",
    author="Ashish Rogannagari",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "pandas==1.3.3",
        "numpy==1.21.2",
        "scipy==1.7.1",
        "scikit-learn==0.24.2",
        "jupyter==1.0.0",
        "seaborn==0.11.2",
        "matplotlib==3.4.3",
        "wordcloud==1.10.3",
    ],
    entry_points={
        "console_scripts": [
            "Data-Aggregation-Grouping-Reshaping-Analysis = src",
            "Output file name: Customersegmentationoutput.ipynb",
            "Input file name: Customersegmentationinput.csv",
        ],
    },
)
