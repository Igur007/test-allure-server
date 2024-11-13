import invoke


@invoke.task
def install(context):
    context.run("uv sync")


@invoke.task
def install_dev(context):
    context.run("uv sync --extra dev")
    # context.run("uv run pre-commit install")


@invoke.task
def check_style(context):
    context.run("uv run ruff check .")


@invoke.task
def tests(context):
    context.run("pytest tests/ -n2 -vv -r xsX --capture=sys --tb=short --alluredir=./allure-results ")


@invoke.task
def tests_coverage(context):
    context.run("pytest tests/unit --cov=harness -x -s")
