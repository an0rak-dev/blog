"""
Entrypoint of the application
"""

import inout as io
import pages
import projectfs as project_filesystem
from jinja2 import Environment, FileSystemLoader


def render_page(style_path, content):
    """
    Render the given content inside the base web page.

    style_path: the custom CSS for this page to add in the webpage
    content: the content to render in the <main> part of the webpage
    """
    templates_dir = project_filesystem.get_templates_directory()
    fs_loader = FileSystemLoader(templates_dir)
    jinja_env = Environment(loader=fs_loader)
    page = jinja_env.get_template("base.html")
    return page.render(style=style_path, main=content)


def main():
    """
    Entrypoint of the app.
    """
    io.setup_dist_directory()
    for static_page in pages.STATIC_PAGES:
        content = io.read_html_content(static_page["input_content"])
        page = render_page(static_page["style"], content)
        io.write_webpage(static_page["output_name"], page)


if __name__ == "__main__":
    main()
