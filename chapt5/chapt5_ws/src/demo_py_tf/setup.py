from setuptools import find_packages, setup

package_name = 'demo_py_tf'

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
            'static_tf_broadcaster=demo_py_tf.static_tf_broadcaster:main',
            'dynamic_tfbroadcaster=demo_py_tf.dynamic_tfbroadcaster:main',
            'tf_listener=demo_py_tf.tf_listener:main'
        ],
    },
)
