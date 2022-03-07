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
module: cp_gaia_diagnostics_facts
author: Stephan Blanke (@stephanblanke)
description:
- Show diagnostics
short_description: Show diagnostics
version_added: '1.0.0'
options:
  category:
    description: category name to show.
    required: true
    type: str
  topic:
    description: topic name to show.
    required: true
    type: str

"""

EXAMPLES = """
- name: Show diagnostics
  cp_gaia_diagnostics_facts:

- name: Show interface by specifying it name
  cp_gaia_diagnostics_facts:
    category: os
    topic: memory

"""

RETURN = """
ansible_facts:
  description: The diagnostics facts.
  returned: always.
  type: list
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import facts_api_call


def main():
    # arguments for the module:
    fields = dict(
        category=dict(required=True, type="str"),
        topic=dict(required=True, type="str")
    )
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = "diagnostics"
    keys = ["category", "topic"]
    res = facts_api_call(module, api_call_object, keys)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
