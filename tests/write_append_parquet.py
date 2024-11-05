from datetime import datetime, timezone
from datetime import timedelta
from decimal import Decimal

from pyspark.sql import SparkSession
from pyspark.sql.types import ArrayType
from pyspark.sql.types import BinaryType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DateType
from pyspark.sql.types import DecimalType
from pyspark.sql.types import DoubleType
from pyspark.sql.types import FloatType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import LongType
from pyspark.sql.types import MapType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType
from pyspark.sql.types import TimestampType

result_file = "./parquet/new"


def run() -> None:
    spark: SparkSession = (
        SparkSession.builder
        .appName("Spark write date Parquet application")
        .getOrCreate()
    )

    df1_schema = StructType(
        [
            StructField("id", StringType(), True),
            StructField("name", StringType(), True),
            StructField("year", IntegerType(), True),
        ],
    )

    data = [
        {"id": "3", "name": "Dilan", "year": 2007},
        {"id": "4", "name": "Michael", "year": 2030},
        {"id": "5", "name": "Tobi U.", "year": 2029},
    ]

    data_frame = spark.createDataFrame(data=data, schema=df1_schema)

    data_frame.printSchema()
    data_frame.show(truncate=False)
    data_frame.repartition(1).write.mode("overwrite").parquet(result_file)


def run2() -> None:
    schema = StructType(
        [
            StructField("id", BinaryType(), True),
            StructField("name", FloatType(), True),
            StructField("year", FloatType(), True),
        ]
    )

    spark = SparkSession.builder.getOrCreate()
    df = spark.createDataFrame(
        [
            (b"foo", 1900.404413386, 1234.3),
            (b"bar", 2000.28563, 2012.2),
        ],
        schema,
    )

    df.repartition(1).write.format("parquet").mode("append").save("temp.parquet")

    spark.read.parquet("temp.parquet").show(truncate=False)
    spark.read.parquet("temp.parquet").printSchema()


def run3() -> None:
    schema = StructType(
        [
            StructField("id", LongType(), True),
            StructField("array", ArrayType(BinaryType(), True), True),
            StructField("bigint", LongType(), True),
            StructField("boolean", BooleanType(), True),
            StructField("date", DateType(), True),
            StructField("decimal", DecimalType(), True),
            StructField("double", DoubleType(), True),
            StructField("integer", IntegerType(), True),
            StructField("map", MapType(
                keyType=BinaryType(),
                valueType=MapType(
                    keyType=BinaryType(),
                    valueType=MapType(
                        StringType(),
                        ArrayType(BinaryType(), True)
                    ),
                    valueContainsNull=True),
                valueContainsNull=True
            ), True),
            StructField("real", FloatType(), True),
            StructField("timestamp", TimestampType(), True),
            StructField("uuid", StringType(), True),
            StructField("varchar", StringType(), True),
            StructField("varbinary", BinaryType(), True),
        ]
    )
    spark = SparkSession.builder.getOrCreate()

    df = spark.createDataFrame(
        [
            (1,
             [b"test 1", None, b"test 101"],
             9007199254740991, True,
             datetime(1971, 1, 13),
             Decimal(3.15), 3.141592653589793, 1,
             {
                 b"test 1": {
                     b"test 1": {
                         "array": [b"test 1", None]
                     }
                 }
             },
             3.141592653589793,
             datetime(2022, 12, 29, 14, 12, 46, 123324, tzinfo=timezone(-timedelta(hours=5, minutes=30))),
             "550e8400-e29b-41d4-a716-446655440001",
             "test 1",
             b"test 1"),
        ],
        schema,
    )

    path_to_file = "temp.parquet"

    spark.read.parquet(path_to_file).show(truncate=False)
    spark.read.parquet(path_to_file).printSchema()


if __name__ == "__main__":
    run()
    run2()
    run3()
