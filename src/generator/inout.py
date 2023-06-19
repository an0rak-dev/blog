"""
Manages the input/output operations for the generator.
"""

# pylint: disable=import-error
import os
import shutil
import projectfs as project_filesystem


def read_html_content(file_name):
    """
    Read the content of the given file_name in the content directory and
    return the result.

    file_name: the name of the file to look for in the content directory.
    """
    content_dir = project_filesystem.get_content_directory()
    with open(
        os.path.join(content_dir, file_name), mode="r", encoding="utf-8"
    ) as html_fd:
        html = html_fd.read()
    return html


def write_webpage(page_name, content):
    """
    Write the given content in the given page_name inside the distribution
    directory.

    page_name: the name of the created file in the distribution directory
    content: the content to write in the file
    """
    dist_dir = project_filesystem.get_dist_directory()
    page_path = os.path.join(dist_dir, page_name)
    print(f"Writing page {page_path}")
    with open(page_path, mode="wt", encoding="utf-8") as page_fd:
        page_fd.write(content)


def setup_dist_directory():
    """
    Create the distribution directory and copy all the public assets inside
    it.
    """
    dist_dir = project_filesystem.get_dist_directory()
    assets_dir = project_filesystem.get_assets_directory()
    target_dir = os.path.join(dist_dir, "assets")
    if not os.path.isdir(dist_dir):
        os.mkdir(dist_dir)
    print(f"Copying assets directory to {target_dir}")
    shutil.copytree(assets_dir, target_dir, dirs_exist_ok=True)
