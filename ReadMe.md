# Blog

My personal Blog.

This repository contains all the resources for my personal [blog](https://an0rak.dev).

## How it works

This blog is composed only by static web pages. Those web pages are generated using 
[Jinja2 templates](https://pypi.org/project/Jinja2) during the CI phase. Those pages
are then committed to a specific `/prod` branch which will deploy them using 
[GitHub Pages](https://pages.github.com/).

Readers can then interact between each other and me using 
[GitHub Discussions](https://github.com/features/discussions).

## Local development

You can follow the tips and procedure [here](./misc/local-development.md).

## Credits and License

This project was created by Sylvain Nieuwlandt, and released under the Apache 2.0 
License. You can find a complete copy of this License [here](./LICENSE). 

Excepting my own logo, all the SVG icons are made by 
[The Pictogrammers Team](https://www.iconarchive.com/artist/pictogrammers.html) and
distributed under the Apache 2.0 License, which you can find 
[here](./misc/icons-license.txt).