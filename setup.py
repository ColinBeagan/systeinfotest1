from setuptools import setup

setup(name="systeminfotest1", 
      version="0.1", 
      description="Basic system information for COMP30830", 
      url="",
      authors="Colin Beagan",
      author_email="colin.beagan@ucdconnect.ie", 
      license="GPL3", 
      packages=['systeminfotest1'],
      entry_points={
          'console_scripts':['comp30830_systeminfo=systeminfotest1.main:main']
          }
      )