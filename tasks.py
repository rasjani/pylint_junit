# flake8: noqa
from invoke import task, Collection
from pathlib import Path
import os

to_be_checked = ["tasks.py", "src/"]
assert Path.cwd() == Path(__file__).parent


def _files():
  return " ".join(to_be_checked)


@task
def format(ctx):
  print("Formatting with ruff")
  ctx.run(f"ruff format {_files()}")


@task
def build(ctx):
  ctx.run("pdm build")


@task
def formatcheck(ctx):
  print("Check format with ruff")
  ctx.run(f"ruff format --check --diff {_files()}")


@task
def ruff(ctx):
  print("Running ruff")
  ctx.run(f"ruff check {_files()}")


@task(post=[ruff])
def check(ctx):
  print("Running all checks")


@task
def test(ctx):
  ctx.run("python -m pytest")
