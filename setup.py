from setuptools import setup, find_packages

setup(
    name="sstv_project",
    version="0.1.0",
    description="A project implementing SSTV encoding and decoding",
    author="KrDevanshu06",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "Pillow",
        "numpy",
        "scipy",
        "soundfile"
    ],
    entry_points={
        "console_scripts": [
            "sstv=main:main"
        ]
    },
)
