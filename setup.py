
import io
from os.path import dirname, join

from setuptools import find_packages, setup

about = {}
with io.open(
        join(dirname(__file__), "src", "py42", "__version__.py"),
        encoding='utf8'
    ) as fh:
        exec(fh.read(), about)


setup(
    name="py42",
    version=about["__version__"],
    description="Official Code42 API Client",
    packages=find_packages("src"),
    package_dir={'': 'src'},
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4",
    install_requires=["requests>=2.3"],
    license="MIT",
    include_package_data=True,
    zip_safe=False,
    extras_require={
        "dev": [
            "pre-commit==1.18.3",
            "pytest==4.6.5",
            "sphinx==1.8.5",
            "tox==3.14.0"
        ]
    }
)
