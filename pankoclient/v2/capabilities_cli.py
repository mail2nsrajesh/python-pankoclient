#   Copyright 2016 Huawei, Inc. All rights reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#

"""Panko v2 Capabilities action implementations"""

from osc_lib.command import command


class CliCapabilitiesList(command.ShowOne):
    """List capabilities for event service"""

    def take_action(self, parsed_args):
        ac = self.app.client_manager.event
        caps = ac.capabilities.list()
        return self.dict2columns(caps._info)
