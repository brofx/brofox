Making Changes
==============

The site is a pretty simple static site. We do use [staticninja][1] to generate the files though.

The only files you should need to edit are in either the `templates` or `static` directory. The html files in the root directory are the generated files.

Setting up the environment
-------------------------

More details instructions to come, but basically create a python virtual environment and install staticjinja:

`pip install staticjinja`

After that you should be good to go.


Compiling the HTML
------------------

Run `staticjinja build` and all the templates will be compiled. After that you are all set!

[1]: https://github.com/Ceasar/staticjinja "staticjinja"