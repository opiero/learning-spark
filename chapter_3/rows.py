from pyspark.sql import Row
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SparkByExamples.com").getOrCreate()

blog_row = Row(6, "Reynold", "Xin", "https://tinyurl.6", 255568, "3/2/2015", ["twitter", "LinkedIn"])

rows = [Row("Matei Zaharia", "CA"), Row("Reynold Xin", "CA")]
authors_df = spark.createDataFrame(rows, ["Authors", "State"])
authors_df.show()
