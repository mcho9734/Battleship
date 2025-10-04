import pytest

def trans(x):
    return str(x)

def apply_names(func, args, tests, noparens=False):
    cases = []
    for case in tests:
        extra = ", ".join(args[i] + trans(x) for i, x in enumerate(case) if (args[i] is not True and args[i] is not False))
        cases.append(
            pytest.param(
                *case, id=func + ("(" if not noparens else "") + ", ".join(trans(x) for i, x in enumerate(case) if args[i] is True) + (")" if not noparens else noparens) + ((", " + extra) if extra else "")
            )
        )
    return cases