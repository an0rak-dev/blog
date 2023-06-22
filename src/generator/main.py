"""
Entrypoint of the application
"""

# pylint: disable=import-error
import argparse
import inout as io
import pages
import projectfs as project_filesystem
import jinja2 as jinja

def render_page(base_url, style_path, content):
    templates_dir = project_filesystem.get_templates_directory()
    fs_loader = jinja.FileSystemLoader(templates_dir)
    template_env = jinja.Environment(loader=fs_loader)
    template = template_env.get_template("base.html")
    base_render = template.render(base=base_url, style=style_path, main=content)
    return template_env.from_string(base_render).render(base=base_url)


def main(base_url):
    """
    Entrypoint of the app.

    base_url: the base url used in all absolute links referencing the generated website.
    """
    io.setup_dist_directory(base_url)
    for static_page in pages.STATIC_PAGES:
        content = io.read_html_content(static_page["input_content"])
        page = render_page(base_url, static_page["style"], content)
        io.write_webpage(static_page["output_name"], page)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("baseUrl", help="The base URL to use in generated html files")
    arguments = parser.parse_args()
    main(arguments.baseUrl)
