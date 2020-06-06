from setuptools import setup

setup(
    name='gca',
    include_package_data=True,
    install_requires=[
        "flask",
        "mongoengine",
        "pymongo",
        "jsonschema",
        "password_strength",
        "twilio",
        "blinker",
        "wheel",
        "pyjwt",
        "middleware"
        "pytest",
        "coverage"
    ],
    tests_require=[
         'pytest',
    ]
)
