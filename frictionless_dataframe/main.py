from dataclasses import dataclass
from io import BytesIO
from typing import Sequence

import pandas
import polars
from frictionless import Package


# https://docs.python.org/3/library/dataclasses.html
@dataclass
class MyResource:
    name: str
    columns: Sequence[str]


def frictionless_to_polars(bytes: bytes, columns: Sequence[str]) -> polars.DataFrame:
    # https://pola-rs.github.io/polars/py-polars/html/reference/api/polars.scan_csv.html#polars.scan_csv
    # return polars.scan_csv(resource.path, columns=columns)
    return polars.read_csv(bytes, columns=columns)


def frictionless_to_pandas(bytes: bytes, columns: Sequence[str]) -> pandas.DataFrame:
    # keep_default_na=False, na_values=[""], sep=",", decimal="."
    # engine="pyarrow"
    return pandas.read_csv(BytesIO(bytes), usecols=columns)


def main() -> None:
    package = Package("datapackage.zip")
    resources = [MyResource(name="currencies", columns=["currency", "symbol"])]

    for resource in resources:
        bytes = package.get_resource(resource.name).read_bytes()

        polars_dataframe = frictionless_to_polars(bytes, resource.columns)
        print("Polars dataframe:\n", polars_dataframe)

        pandas_dataframe = frictionless_to_pandas(bytes, resource.columns)
        print("Pandas dataframe:\n", pandas_dataframe)


if __name__ == "__main__":
    main()
