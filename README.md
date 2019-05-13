# cookiecutter-active-data-recipes

This repository provides a template for creating new [active-data-recipe][0] based projects.
ActiveData recipes are bundled into two parts:

1. The [recipe runner][1] called `adr`.
2. The recipe repositories (where recipes are stored).

There are many different repositories of recipes, owned and maintained by various teams across
Mozilla. There is also an [official][2] repository, but this exists mostly for historical reasons
and example purposes.

This cookiecutter will help you create your very own `active-data-recipes` repository.

# Usage

Run:

    $ pip install cookiecutter
    $ cookiecutter ahal/cookiecutter-active-data-recipes

Then answer the prompts to fill out some required metadata. When picking your `project_name` be
aware that it should be separated by dashes and will have `-recipes` automatically appended to the
end of it.

For example, if you call your project `perf-test`, a project directory called `perf-test-recipes`
will be created. See the [cookiecutter][3] documentation for more information.

# Features

This project template includes:

1. [Poetry][4] to manage packaging and depdendies.
2. [Pytest][5] to run tests.
3. [Flake8][6] for linting (with `flake8-import-order` installed).
4. [Sphinx][7] for building documentation.
5. A custom `doclint` linter to make sure recipes are documented.
6. A bash completion script under `extra`.
7. [TravisCI][8] and [tox][9] configs to handle CI.
8. An example recipe and query (with copious comments) to help get you started.

# What to Do Next

After generating the project, a working example recipe and associated test will be generated for
you. The first thing to do is make sure you can run them:

    $ poetry install
    $ poetry shell
    $ adr example
    # should see recipe output

You can run the tests + linters with:

    $ tox

If you want CI and documentation, you'll need to hook up the repository to [TravisCI][8] and
[readthedocs][10] respectively. If you don't need these, feel free to delete the relevant config
files.

Finally, take a look at the example recipe and query. They have lots of comments that explain the
various aspects of a `recipe`. You can either modify this to suit your needs or create a new recipe
from scratch. Take a look at the main [active-data-recipe][0] documentation for more information on
writing recipes and queries.

[0]: https://active-data-recipes.readthedocs.io/en/latest/
[1]: https://pypi.org/project/adr
[2]: https://github.com/mozilla/active-data-recipes
[3]: https://cookiecutter.readthedocs.io/en/latest/
[4]: https://poetry.eustace.io/
[5]: https://docs.pytest.org/en/latest/index.html
[6]: http://flake8.pycqa.org/en/latest/
[7]: http://www.sphinx-doc.org/en/master/
[8]: https://docs.travis-ci.com/
[9]: https://tox.readthedocs.io/en/latest/
[10]: https://readthedocs.org/
