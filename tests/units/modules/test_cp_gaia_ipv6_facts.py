
# Ansible module to manage CheckPoint Firewall (c) 2019
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

from __future__ import absolute_import, division, print_function
__metaclass__ = type
import pytest
from units.modules.utils import set_module_args, exit_json, fail_json, AnsibleExitJson
from ansible.module_utils import basic
from ansible_collections.check_point.gaia.plugins.modules import cp_gaia_ipv6_facts

EXPECTED_RESULT = {
    "reboot-required": False,
    "enabled": True
}

PAYLOAD = {}

function_path = 'ansible_collections.check_point.gaia.plugins.modules.cp_gaia_ipv6_facts.chkp_facts_api_call'
api_call_object = 'ipv6'


class TestCheckpointIpv6Facts(object):
    module = cp_gaia_ipv6_facts

    @pytest.fixture(autouse=True)
    def module_mock(self, mocker):
        return mocker.patch.multiple(basic.AnsibleModule, exit_json=exit_json, fail_json=fail_json)

    @pytest.fixture
    def connection_mock(self, mocker):
        connection_class_mock = mocker.patch('ansible.module_utils.network.checkpoint.checkpoint.Connection')
        return connection_class_mock.return_value

    def test_facts(self, mocker, connection_mock):
        mock_function = mocker.patch(function_path)
        mock_function.side_effect = [{
            "changed": False,
            api_call_object: EXPECTED_RESULT
        }
        ]
        result = self._run_module(PAYLOAD)
        assert not result['changed']
        assert EXPECTED_RESULT.items() == result[api_call_object].items()

    def _run_module(self, module_args):
        set_module_args(module_args)
        with pytest.raises(AnsibleExitJson) as ex:
            self.module.main()
        return ex.value.args[0]
