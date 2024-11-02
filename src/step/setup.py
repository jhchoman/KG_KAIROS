from setuptools import setup
import os
from glob import glob

package_name = 'step'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.urdf')),  # urdf만 포함
    ],
    install_requires=[
        'setuptools',
        'pyserial',  # pyserial 추가
    ],
    zip_safe=True,
    maintainer='jhchoman',
    maintainer_email='jhchoman@todo.todo',
    description='Description of the package',
    license='License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'twist_listener_node = step.twist_listener_node:main',
        ],
    },
)
