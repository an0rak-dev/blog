import os
import shutil
import projectfs as project_filesystem


def read_html_content(file_name):
    content_dir = project_filesystem.get_content_directory()
    with open(os.path.join(content_dir, file_name), mode="r", encoding="utf-8") as html_fd:
        html = html_fd.read()
    return html



def write_webpage(page_name, content):
    dist_dir = project_filesystem.get_dist_directory()
    page_path = os.path.join(dist_dir, page_name)
    print(f"Writing page {page_path}")
    with open(page_path, mode="wt", encoding="utf-8") as page_fd:
        page_fd.write(content)


def setup_dist_directory():
    dist_dir = project_filesystem.get_dist_directory()
    assets_dir = project_filesystem.get_assets_directory()
    if not os.path.isdir(dist_dir):
        os.mkdir(dist_dir)
    shutil.copytree(assets_dir, os.path.join(dist_dir, "assets"), dirs_exist_ok=True)
