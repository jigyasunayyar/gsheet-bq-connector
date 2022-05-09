from typing import Callable


def transfunctiondecorator(
        customfunc:Callable)->Callable:
    def wrapper(pd_df, *args, **kwargs):
        customfunc.__globals__["pd_df"] = pd_df
        return customfunc()

    return wrapper

@transfunctiondecorator
def transformlucanet():
    import pandas as pd
    pd.set_option('display.max_columns', None)
    # print(pd_df.to_markdown())
    print(pd_df.head(10))

    return pd_df
