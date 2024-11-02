from setuptools import find_packages, setup

package_name = 'my_int64_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
            'int64_publisher = my_int64_pkg.int64_publisher:main',
            'int64_subscriber = my_int64_pkg.int64_subscriber:main',
        ],
    },
)
