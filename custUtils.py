import pandas as pd
from typing import Optional
from transformConfig import TransformConfig


def pushtobq(
        pd_df: pd.DataFrame,
        tablename: str = 'bl_europe_sheets.gsheet-bq-test',
        project: str = 'dhh---analytics-eu',
        chunksize: Optional[int] = None,
        if_exists: Optional[str] = "replace"
) -> None:
    """
    Push pandas dataframe to bigquery table.
    :param pd_df: pandas DF
    :param tablename: bigquery table name
    :param project: bigquery project
    :param chunksize: rows chunksize
    :param if_exists: Table overriding rules
    :return: None
    """

    return pd_df.to_gbq(tablename,
                        project,
                        chunksize=chunksize,
                        if_exists=if_exists)

def runtransform(
        config: TransformConfig
):
    """

    :param config:
    :return:
    """
    path = config.filepath
    table_name = config.table_name

    transform_func = config.transform_func
    df_pd = pd.read_excel(path)

    # df_pd.head(10)
    # print(df_pd.shape)
    df_pd = transform_func(df_pd)
    # print(df_pd.columns)
    # print(df_pd.info)
    pushtobq(df_pd, table_name, **config)


def extractconfig(
        runlist:Optional[list[str,...]]
):
    """

    :param runlist:
    :return:
    """
    if runlist:
        for processname in runlist:
            try:
                # config = [config for config in transformsheets if config.process_name == processname][0]
                exec(f"from transformConfig import {processname} as sheet", globals())
            except ImportError:
                raise ImportError(f"{process_name} missing in the transform config. please add config.")
                continue
            runtransform(sheet)

    else:
        from transformConfig import transformsheets
        for sheet in transformsheets:
            runtransform(sheet)



