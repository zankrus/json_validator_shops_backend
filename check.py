
Пflake8 --max-line-length=120 .
pep257 .
pep 484
mypy . --disallow-untyped-calls --disallow-untyped-defs --disallow-incomplete-defs --check-untyped-defs  --disallow-untyped-decorators --ignore-missing-imports --pretty

vulture . --min-confidence 70
radon mi -m .

