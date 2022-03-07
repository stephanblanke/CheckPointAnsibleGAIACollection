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

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = """
module: cp_gaia_asset_facts
author: stephanblanke (@stephanblanke)
description:
- Show assets
short_description: Show assets
version_added: '1.0.0'
"""

EXAMPLES = """
- name: Show assets
  cp_gaia_asset_facts:

"""

RETURN = """
ansible_facts:
  description: The asset facts.
  returned: always.
  type: list
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import api_call


def main():
    # arguments for the module:
    fields = dict()
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    res = api_call(module=module, api_call_object="show-asset")
    module.exit_json(ansible_facts=res)


if __name__ == "__main__":
    main()
