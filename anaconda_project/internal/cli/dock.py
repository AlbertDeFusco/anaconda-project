# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2019, Anaconda, Inc. All rights reserved.
#
# Licensed under the terms of the BSD 3-Clause License.
# The full license is in the file LICENSE.txt, distributed with this software.
# -----------------------------------------------------------------------------
"""The ``dock`` command creates a docker image of the desired project"""
from __future__ import absolute_import, print_function

from anaconda_project.internal.cli.project_load import load_project
from anaconda_project.internal.cli import console_utils
from anaconda_project import project_ops


def dock_command(
        project_dir,
        tag,
        command,
        dockerfile_path,
        condarc_path,
        build_args
):
    """Build docker image

    Returns:
        exit code
    """
    project = load_project(project_dir)
    status = project_ops.dock(project, tag=tag, command=command,
                              dockerfile_path=dockerfile_path,
                              condarc_path=condarc_path, build_args=build_args)
    if status:
        print(status.status_description)
        return 0
    else:
        console_utils.print_status_errors(status)
        return 1


def main(args):
    """Start the docker build command and return exit status code."""
    return dock_command(args.directory, args.tag, args.command,
                        args.dockerfile_path, args.condarc_path,
                        args.build_args)
