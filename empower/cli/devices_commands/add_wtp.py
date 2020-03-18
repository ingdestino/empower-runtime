#!/usr/bin/env python3
#
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.

""" Help CLI tools."""

import argparse

from empower.cli import command

from empower.core.etheraddress import EtherAddress

# CLI Command Name
NAME = "add-wtp"

# CLI Command Description
DESC = "Add a new WTP."

# CLI Command Function Pointers (parser, exec)
PARSER = "pa_add_wtp"
EXEC = "do_add_wtp"


def pa_add_wtp(args, cmd):
    """Add WTP parser method. """

    usage = "%s <options>" % command.USAGE.format(cmd)
    desc = command.DESCS[cmd]

    parser = argparse.ArgumentParser(usage=usage, description=desc)

    required = parser.add_argument_group('required named arguments')

    required.add_argument('-a', '--addr', help='The device address',
                          required=True, type=EtherAddress, dest="addr")

    parser.add_argument("-d", "--desc", dest="desc", type=str, default=None,
                        help="A human readable description of the device")

    (args, leftovers) = parser.parse_known_args(args)

    return args, leftovers


def do_add_wtp(gargs, args, _):
    """ Add a new WTP """

    request = {
        "version": "1.0",
        "addr": args.addr
    }

    if args.desc:
        request["desc"] = args.desc

    headers = command.get_headers(gargs)

    url = '/api/v1/wtps'
    command.connect(gargs, ('POST', url), 201, request, headers=headers)

    print(args.addr)
