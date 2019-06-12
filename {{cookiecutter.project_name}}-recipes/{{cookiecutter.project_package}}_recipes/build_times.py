"""
Get build task runtimes. Returns the total count, average runtime and total
runtime over a given date range and set of branches.

.. code-block:: bash

    adr build_times [--from-date <date>] [--to-date <date>] [--branch <branch>]

"""
import argparse
from adr.context import override
from adr.query import run_query
from loguru import logger

DEFAULT_BRANCHES = [
    'autoland',
    'mozilla-central',
    'mozilla-inbound',
]

# The RUN_CONTEXTS global contains context definitions that are unique to this
# recipe.
RUN_CONTEXTS = [
    # Sometimes the shared context needs to be tweaked (in this case, let's
    # remove '--kind' from the help since it will be hardcoded later on. This
    # can be accomplished with the 'override' method.
    override('kind', help=argparse.SUPPRESS)
]


# All recipes must have a 'run' function. The 'args' value contains all of the
# context needed by this recipe and the queries that it uses. Context can be
# accessed using dot notation (e.g, args.foo).
def run(args):
    logger.info("Running the 'build_times' recipe!")

    # The task_durations query was designed to be more general purpose than
    # this recipe. Since we are only looking at build tasks here, we can hard
    # code the 'kind' context.
    args.kind = "build"

    # Set the default branch if it wasn't specified.
    args.branches = args.branches or DEFAULT_BRANCHES

    # The 'run_query' function will run the specified query (named in the
    # 'queries' directory) using the specified context. Often you can just
    # forward 'args' wholesale, but you can also build the context manually if
    # necessary. In more complicated cases the output of one query might
    # determine the context of another.
    data = run_query('task_durations', args)['data']

    # The above query returns a list of values of the form:
    # [<build label>, <number of tasks>, <average runtime>]
    result = []
    for record in data:
        # ActiveData can sometimes return missing records or erroneous values.
        # Sometimes data sanitization is needed.
        if record[2] is None:
            continue

        # Compute the total hours spent running each build by multiplying
        # number of tasks by average runtime.
        record.append(int(round(record[1] * record[2], 0)))
        result.append(record)

        # Round the average hours.
        record[2] = round(record[2])

        # In this case, we don't care about the number of tasks after
        # calculating the total.
        del record[1]

    # Sort the results by average runtime.
    result = sorted(result, key=lambda k: k[1], reverse=True)

    # Insert a header.
    result.insert(0, ['Build', 'Average (min)', 'Total (min)'])

    # Return the result to be formatted into a table by adr. In this case the
    # structure of result looks like:
    # [
    #   [ "HeaderA", "HeaderB", "HeaderC"],
    #   [ "Row1 Col1", "Row1 Col2", "Row1 Col3"],
    #   [ "Row2 Col1", "Row2 Col2", "Row2 Col3"],
    #   etc..
    # ]
    return result
