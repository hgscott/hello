# hello

A minimal example repository used in the "Continuous Curation" guide for
[MIT1002-GEM](https://github.com/C-CoMP-STC/MIT1002-GEM) to show how to write a
unit test and run it automatically with GitHub Actions.

- `hello.py` — the function being tested
- `tests/test_hello.py` — its unit tests (`unittest`)
- `.github/workflows/test-hello.yml` — the GitHub Actions workflow that runs the tests on every push

Run the tests locally from the top of the repository with either:

```bash
python -m unittest
pytest
```
