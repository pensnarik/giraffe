import os
import pwd
import grp

from setuptools import setup, Command
from setuptools.command.install import install
from distutils.util import convert_path

def prepare():
    if os.getuid() != 0:
        # This means we run in virtualenv
        return

    try:
        grp.getgrnam('giraffe')
    except KeyError:
        os.system('groupadd giraffe')

    try:
        pwd.getpwnam('giraffe')
    except KeyError:
        os.system('useradd giraffe -g giraffe --shell /usr/sbin/nologin')

    if not os.path.exists('/var/log/giraffe'):
        os.mkdir('/var/log/giraffe')

    os.system('chown giraffe:giraffe /var/log/giraffe')
    os.system('chmod g+w /var/log/giraffe')

    print('User giraffe and directory /var/log/giraffe have been created successfully')

def get_version():
    d = {}
    with open('libgiraffe/__init__.py') as fp:
        exec(fp.read(), d)

    return d["__version__"]

class PrepareUser(Command):

    description = 'Creates the user'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        prepare()

class PrepareInstall(install):

    def run(self):
        prepare()
        install.run(self)

setup(name="giraffe-watchdog",
      description="Giraffe watchdog tools",
      license="MIT",
      version=get_version(),
      maintainer="Andrey Zhidenkov",
      maintainer_email="pensnarik@gmail.com",
      url="http://parselab.ru",
      scripts=['giraffe'],
      packages=['libgiraffe'],
      install_requires=["psycopg2", "requests", "pyyaml"],
      data_files=[('etc/giraffe.d', ['basic.yml'])],
      cmdclass={'prepare': PrepareUser, 'install': PrepareInstall}
)
