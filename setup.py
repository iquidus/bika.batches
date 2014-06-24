from setuptools import setup, find_packages

version = '1.0'

setup(name='bika.batches',
      version=version,
      description='Bika LIMS extension',
      long_description=open('README.md').read(),
      classifiers=[
          'Framework :: Plone',
          'Programming Language :: Python',
      ],
      keywords='Bika Open Source LIMS Iquidus',
      author='Iquidus Technology',
      author_email='info@iquidus.co.nz',
      url='www.iquidus.co.nz',
      license='AGPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['bika'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'bika.lims',
          'archetypes.schemaextender',
      ],
      extras_require={
          'test': [
              'plone.app.testing',
              'robotsuite',
              'robotframework-selenium2library',
              'plone.app.robotframework'
          ]
      },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
