from setuptools import find_packages, setup

package_name = 'esp32_bridge_w2s'

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
    maintainer='u',
    maintainer_email='u@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'esp32_bridge_w2s = esp32_bridge_w2s.esp32_bridge_w2s:main',
        	'esp32_teleop = esp32_bridge_w2s.esp32_teleop:main',
        	
        ],
    },
)
