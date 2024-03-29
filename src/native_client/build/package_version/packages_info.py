#!/usr/bin/python
# Copyright (c) 2014 The Native Client Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Encompasses a description of packages associated with package targets."""

import json


def LoadJSONStripComments(file):
  lines = []
  for line in file.readlines():
    line = line.rstrip()
    comment_index = line.find('#')
    if comment_index != -1:
      lines.append(line[:comment_index])
    else:
      lines.append(line)

  stripped_file = '\n'.join(lines)
  return json.loads(stripped_file)


class PackagesInfo(object):
  """A packages file is a JSON file describing package targets and packages."""
  def __init__(self, packages_file):
    if isinstance(packages_file, basestring):
      with open(packages_file, 'rt') as f:
        packages_json = LoadJSONStripComments(f)
    elif isinstance(packages_file, file):
      packages_json = LoadJSONStripComments(packages_file)
    else:
      raise RuntimeError('Invalid packages file type (%s): %s' %
                         (type(packages_file), packages_file))

    assert isinstance(packages_json, dict), (
        "Invalid packages file: %s" % packages_file)

    self._platform_targets = packages_json.get('package_targets', {})
    self._shared_packages = set(packages_json.get('shared',[]))
    self._packages = packages_json.get('packages',{})

  def IsSharedPackage(self, package_name):
    """Returns whether or not a package is shared between all host platforms.

    Args:
      package_name: Name of a package.
    Returns:
      True if a package is shared, False otherwise.
    """
    return package_name in self._shared_packages

  def GetPackageTargets(self, host_platform, host_arch):
    """Returns a list of package targets for a given host.

    Args:
      host_platform: Normalized host platform name from pynacl.platform.
      host_arch: Normalized host architecture name from pynacl.platform.
    Returns:
      List of package targets for platform/arch, empty list if not defined.
    """
    return self._platform_targets.get(host_platform, {}).get(host_arch, [])

  def GetPackages(self, package_target):
    """Returns the list of packages for a given package target.

    Args:
      package_target: Valid package target as defined in the packages file.
    Returns:
      List of packages for a package target. None if invalid package target.
    """
    return self._packages.get(package_target, None)

  def GetPackageTargetsForPackage(self, package):
    """Returns a list of all host platforms which is a toolchain component.

    Args:
      component: A toolchain component.
    Returns:
      List of host platforms which use the toolchain component.
    """
    return [package_target
            for package_target, packages
            in self._packages.iteritems()
            if package in packages]
