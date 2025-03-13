import os

# nose2
os.system(
    "nose2 --with-coverage --coverage pyvchart " "--coverage-config .coveragerc -s test"
)

# pytest
os.system("pytest --cov-branch --cov-report=xml -cov-config=.coveragerc --cov=./ test/")

# flake8 for code linting
os.system("flake8 --exclude=build,example,images --max-line-length=89 --ignore=F401")
