from setuptools import find_packages, setup
from glob import glob
package_name = 'demo_python_service'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name+ "/resource", ['resource/default.jpeg', 'resource/test1.jpeg']),
        ('share/' + package_name+ "/launch", glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='xlp',
    maintainer_email='2659037268@qq.com',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'learn_face_detect=demo_python_service.learn_face_detect:main',
            'face_detect_node=demo_python_service.face_detect_node:main',
            'face_detect_client_node=demo_python_service.face_detect_client_node:main',
        ],
    },
)
