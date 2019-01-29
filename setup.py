from setuptools import setup

setup(name="systeminfotest", 
      version="0.1", 
      description="Basic system information for COMP30830", 
      url="",
      authors="Colin Beagan",
      license="GPL3", 
      packages=['systeminfotest'],
      entry_points={
          'console_scripts':['comp30830_systeminfo=systeminfotest.main:main']
          }
      )