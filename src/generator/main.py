import inout as io
import pages
import projectfs as project_filesystem
from jinja2 import Environment, FileSystemLoader


def render_page(style_path, content):
    templates_dir = project_filesystem.get_templates_directory()
    fs_loader = FileSystemLoader(templates_dir)
    jinja_env = Environment(loader=fs_loader)
    page = jinja_env.get_template("base.html")
    return page.render(style=style_path, main=content)


def main():
    io.setup_dist_directory()
    for static_page in pages.STATIC_PAGES:
        content = io.read_html_content(static_page["input_content"])
        page = render_page(static_page["style"], content)
        io.write_webpage(static_page["output_name"], page)


if __name__ == "__main__":
    main()
