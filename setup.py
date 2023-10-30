from distutils.core import setup

setup(name='booklover',
      version='0.1',
      description='Tracks reading lists',
      license = 'MIT',
      url='https://github.com/danS3r/booklover',
      
      # list folders, not files
      packages=['booklover'], # Include packages in the project
      install_requires= ['pandas']
)