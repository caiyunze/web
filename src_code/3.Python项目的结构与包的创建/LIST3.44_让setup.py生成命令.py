from setuptools import setup

setup(
    name='guestbook',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
    ],
    entry_points="""
        [console_scripts]
        guestbook = guestbook:main
    """,
)
