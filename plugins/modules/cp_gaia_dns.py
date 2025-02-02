#!/usr/bin/python
# -*- coding: utf-8 -*-
#
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

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


DOCUMENTATION = """
author: Majd Sharkia (@chkp-majds)
description:
- Setting DNS configuration
module: cp_gaia_dns
short_description: Setting DNS configuration
version_added: '2.0.0'
requirements:
- supported starting from gaia_api >= 1.7
options:

    suffix:
        description: Use empty-string in order to remove the setting
        required: False
        type: str
    primary:
        description: Use empty-string in order to remove the setting
        required: False
        type: str
    tertiary:
        description: Use empty-string in order to remove the setting
        required: False
        type: str
    secondary:
        description: Use empty-string in order to remove the setting
        required: False
        type: str

"""


EXAMPLES = """
- name: Setting dns servers for the system
  cp_gaia_dns:
    "suffix": "checkpoint.com"
    "primary": "1.2.3.4"
    "tertiary": "3.4.5.6"
    "secondary": "2.3.4.5"

"""


RETURN = """
dns:
  description: The checkpoint object updated.
  returned: always.
  type: dict
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import chkp_api_call


def main():
    # arguments for the module:
    fields = dict(
        suffix=dict(type="str"),
        primary=dict(type="str"),
        tertiary=dict(type="str"),
        secondary=dict(type="str")
    )
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'set-dns'
    ansible_release_version = 'v1.6/'

    res = chkp_api_call(module, api_call_object, ansible_release_version)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
