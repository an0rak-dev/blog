import os

def get_generator_directory():
    return os.path.dirname(os.path.realpath(__file__))


def get_src_directory():
    return os.path.dirname(get_generator_directory())


def get_content_directory():
    return os.path.join(get_src_directory(), "contents")


def get_root_directory():
    return os.path.dirname(get_src_directory())


def get_resources_directory():
    return os.path.join(get_root_directory(), "resources")


def get_assets_directory():
    return os.path.join(get_resources_directory(), "assets")


def get_templates_directory():
    return os.path.join(get_resources_directory(), "templates")


def get_dist_directory():
    root_dir = get_root_directory()
    return os.path.join(root_dir, "docs")