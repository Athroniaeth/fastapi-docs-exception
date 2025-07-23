from fastapi_docs_exception.handler import ExceptionResponseFactory


def lint():  # pragma: no cover
    """Development lint function."""
    import subprocess  # nosec: only calling static, internal commands
    import shutil

    ty = shutil.which("ty")
    ruff = shutil.which("ruff")
    bandit = shutil.which("bandit")

    if (ty is None) or (ruff is None) or (bandit is None):
        raise RuntimeError("Please install development dependencies: `uv sync --dev`")

    list_commands = [
        [ruff, "format", "."],
        [ruff, "check", "--fix", "."],
        [ty, "check", "."],
        [bandit, "-c", "pyproject.toml", "-r", "src"],
    ]

    for command in list_commands:
        print(f"Running command: `{' '.join(command)}`")
        subprocess.run(command, check=True, shell=False)  # nosec: B603


__all__ = ["ExceptionResponseFactory"]
