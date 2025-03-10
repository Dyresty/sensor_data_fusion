from setuptools import setup

package_name = 'sensor_data_fusion'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dyresty',
    maintainer_email='rochan-kumar.saravanakannan@stud.hs-coburg.de',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'hsc_gridmap = sensor_data_fusion.gridmap_hsc:test_gridmap_node_checkered',
            'hsc_gridmap_name = sensor_data_fusion.gridmap_hsc:test_gridmap_node_figure',
            'hsc_mapping_sample = sensor_data_fusion.mapping_hsc:mapping_with_sample',
            'hsc_mapping_laser = sensor_data_fusion.mapping_hsc:mapping_with_laser_scan',
        ],
    },
)
