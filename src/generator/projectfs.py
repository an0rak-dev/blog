"""
Expose several functions to map the project's tree structure.
"""

import os


def get_generator_directory():
    """
    Returns the generator's source code directory
    """
    return os.path.dirname(os.path.realpath(__file__))


def get_src_directory():
    """
    Returns the global source directory
    """
    return os.path.dirname(get_generator_directory())


def get_content_directory():
    """
    Returns the pages' content directory.
    """
    return os.path.join(get_src_directory(), "contents")


def get_root_directory():
    """
    Returns the root directory of the project (absolute path).
    """
    return os.path.dirname(get_src_directory())


def get_resources_directory():
    """
    Returns the resources directory (templates & public assets).
    """
    return os.path.join(get_root_directory(), "resources")


def get_assets_directory():
    """
    Returns the public assets directory.
    """
    return os.path.join(get_resources_directory(), "assets")


def get_templates_directory():
    """
    Returns the Jinja templates directory.
    """
    return os.path.join(get_resources_directory(), "templates")


def get_dist_directory():
    """
    Returns the distribution directory where the generated website will
    be written.
    """
    return os.path.join(get_root_directory(), "dist")
