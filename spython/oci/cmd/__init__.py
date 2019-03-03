
# Copyright (C) 2017-2019 Vanessa Sochat.

# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.


def generate_oci_commands():
    ''' The oci command group will allow interaction with an image using
        OCI commands.
    '''
    from spython.oci import OciImage

    from spython.main.base.logger import println
    from spython.utils import run_command as run_cmd

    # run_command uses run_cmd, but wraps to catch error
    from spython.main.base.command import ( run_command, send_command )
    from spython.main.base.generate import RobotNamer

    # Oci Command Groups
    from .mounts import ( mount, umount )
    from .states import ( kill, state, start, resume )
    from .actions import ( attach, create, delete, execute, run, _run, update )

    # Oci Commands
    OciImage.start = start
    OciImage.mount = mount
    OciImage.umount = umount
    OciImage.state = state
    OciImage.resume = resume
    OciImage.attach = attach
    OciImage.create = create
    OciImage.delete = delete
    OciImage.execute = execute
    OciImage.kill = kill
    OciImage.run = run
    OciImage._run = _run
    OciImage.update = update

    OciImage.RobotNamer = RobotNamer()
    OciImage.run_command = run_cmd
    OciImage._send_command = send_command # send and disregard stderr, stdout
    OciImage._run_command = run_command
    OciImage._println = println
 
    return OciImage