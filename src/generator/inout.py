"""
Manages the input/output operations for the generator.
"""

# pylint: disable=import-error
import os
import shutil
import jinja2 as jinja
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


def copy_asset_directory(dir_name : str):
    target_dir = os.path.join(project_filesystem.get_dist_directory(), "assets", dir_name)
    assets_dir = os.path.join(project_filesystem.get_assets_directory(), dir_name)
    print(f"Copying {dir_name} directory to {target_dir}")
    shutil.copytree(assets_dir, target_dir, dirs_exist_ok=True)


def render_asset_directory(dir_name: str, base_url: str):
    target_dir = os.path.join(project_filesystem.get_dist_directory(), "assets", dir_name)
    asset_dir = os.path.join(project_filesystem.get_assets_directory(), dir_name)
    if not os.path.isdir(target_dir):
        os.mkdir(target_dir)
    fs_loader = jinja.FileSystemLoader(asset_dir)
    env = jinja.Environment(loader=fs_loader)
    for filename in os.listdir(asset_dir):
        template_location = os.path.join(target_dir, filename)
        template = env.get_template(filename)
        print(f"Rendering asset {template_location} in {target_dir}")
        content = template.render(base=base_url)
        with open(template_location, encoding="utf-8", mode="wt") as fd:
            fd.write(content)



def setup_dist_directory(base_url: str):
    """
    Create the distribution directory and copy all the public assets inside
    it.

    base_url: The base URL of the website to generate
    """
    dist_dir = project_filesystem.get_dist_directory()
    assets_dir = project_filesystem.get_assets_directory()
    target_dir = os.path.join(dist_dir, "assets")
    if not os.path.isdir(dist_dir):
        os.mkdir(dist_dir)
    copy_asset_directory("fonts")
    copy_asset_directory("images")
    render_asset_directory("styles", base_url)
    render_asset_directory("scripts", base_url)
