import setuptools

setuptools.setup(
    name="monitor",
    packages=setuptools.find_packages(where='src'),
    package_dir = {'':'src'},
    scripts=['bin/monitor'],
    version="0.0.1",
    author="Luke Logan",
    author_email="llogan@hawk.iit.edu",
    description="A simple tool to monitor apps and produce network,disk,cpu logs",
    url="https://github.com/lukemartinlogan/monitor_parsers",
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 0 - Pre-Alpha",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: None",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System Monitoring",
    ],
    long_description=""
)
