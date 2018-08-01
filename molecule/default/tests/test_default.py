import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_repository_file(host):
    f = host.file('/etc/apt/sources.list.d/docker.list')
    assert f.exists is True
