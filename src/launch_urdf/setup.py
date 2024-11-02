from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'launch_urdf'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/urdf_launch.py']),
        (os.path.join('share',package_name,'launch'),glob(os.path.join('launch','*launch.py'))),
        (os.path.join('share',package_name,'urdf'),glob('urdf/*')),
        (os.path.join('share',package_name,'rviz'),glob('rviz/*')),

    ],

    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jhchoman',
    maintainer_email='jhchoman@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'launch_urdf=launch_urdf.launch_urdf:main'
        ],
    },
)
