from pyspark.sql.functions import col, regexp_replace, lit, trim, when
from pyspark.sql.types import IntegerType, DecimalType

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("MyFirstCSVLoad").getOrCreate()
df = spark.read.option("header", True).option("inferSchema", True).csv("C:/BigDataLocalSetup/spark/datasets/bank.csv")

df = df.drop(".")
withdrawalAmtCol = " WITHDRAWAL AMT "
depositAmtCol = " DEPOSIT AMT "
chequeNoCol = " CHQ.NO. "
#
# # DRY - DO NOT REPEAT YOURSELF
#
df = df.na.fill("0", [withdrawalAmtCol, depositAmtCol])
# # df.show()
df = df.withColumn(withdrawalAmtCol, regexp_replace(col(withdrawalAmtCol), ',', '').cast('double'))
df = df.withColumn(depositAmtCol, regexp_replace(col(depositAmtCol), ',', '').cast('double'))
# # df.show(100)
# df.printSchema()
#
df = df.withColumn("TRANSACTION_AMOUNT", col(withdrawalAmtCol) + col(depositAmtCol))
# # # # df = df.withColumn("TRANSACTION AMOUNT", lit("something"))
df = df.withColumn("TRANSACTION_TYPE", when(col(withdrawalAmtCol) != 0.0, "DR").when(col(depositAmtCol) != 0.0, "CR").otherwise("NO TRANSACTION"))
df.show()



# print(df.columns)


# df = df.withColumnRenamed("Account No", "AccountNo")
# df = df.withColumnRenamed("TRANSACTION DETAILS", "TransactionDetails")
# df = df.withColumnRenamed("VALUE DATE", "ValueDate")
# df = df.withColumnRenamed("WITHDRAWAL AMT", "WithdrawalAmt")
# df = df.withColumnRenamed("DEPOSIT AMT", "DepositAmt")
# df = df.withColumnRenamed("BALANCE AMT", "BalanceAmt")
new_column_name_list = list(map(lambda x: x.replace(" ", "_"), df.columns))

df = df.toDF(*new_column_name_list)
print(df.columns)
df = df.withColumn("Account_No", regexp_replace(col("Account_No"), "'", ''))
df.show()

df1 = df.filter(df.TRANSACTION_TYPE == "DR")
df1.show()

df1.coalesce(1).write.mode('overwrite').option("header", "true").parquet("C:/BigDataLocalSetup/spark/datasets/DRTransactionParquet")

df2 = df.filter(df.TRANSACTION_TYPE == "CR")
df2.show()

df2.coalesce(1).write.mode('overwrite').option("header", "true").parquet("C:/BigDataLocalSetup/spark/datasets/CRTransactionParquet")

df = df.withColumnRenamed("CHQ.NO.", "CHQNo")
print(df.columns)
df3 = df.filter(df.CHQNo.isNotNull())
df3.show()
df3.coalesce(1).write.mode('overwrite').option("header", "true").parquet("C:/BigDataLocalSetup/spark/datasets/ChequeTransactionParquet")




# print(df.rdd.getNumPartitions())
# print(df.columns)
# df.write.option("header", True).csv("C:/BigDataLocalSetup/spark/datasets/bank_output.csv")
# df.show()
# df.coalesce(1).write.format("com.databricks.spark.csv").csv("C:/BigDataLocalSetup/spark/datasets/bank_output.csv", mode='overwrite')
# df.coalesce(1).write.mode('overwrite').option("header", "true").parquet("C:/BigDataLocalSetup/spark/datasets/sample2")
# df.coalesce(1).write.mode('overwrite').option("header", "true").csv("C:/BigDataLocalSetup/spark/datasets/sample1")
# df.repartition(1).write.format("csv").mode("overwrite").option("header", True).save("C:/BigDataLocalSetup/spark/output")
# print('completed')

# withdrawalAmtCol = " WITHDRAWAL AMT "
# depositAmtCol = " DEPOSIT AMT "

# def Drop9thEmptyColumn(df):
#     return df.drop(".")
#
#
# def MoveWithDrawalandDepositAmountToTransactionAmount(df):
#     df = df.na.fill("0", [withdrawalAmtCol, depositAmtCol])
#     df = df.withColumn(withdrawalAmtCol, regexp_replace(col(withdrawalAmtCol), ',', '').cast('double'))
#     df = df.withColumn(depositAmtCol, regexp_replace(col(depositAmtCol), ',', '').cast('double'))
#     df = df.withColumn("TRANSACTION AMOUNT", col(withdrawalAmtCol) + col(depositAmtCol))
#     return df
#
#
# def CreateTransactionTypeColumn(df):
#     df = df.withColumn("TRANSACTION TYPE", when(col(withdrawalAmtCol) != 0.0, "DR").when(col(depositAmtCol) != 0.0, "CR").otherwise("NO TRANSACTION"))
#     return df
#
#
# def SaveToCSVFile(df, path):
#     df.coalesce(1).write.mode('overwrite').option("header", "true").csv(path)
#
#
#
# def DoStep1(df):
#     df = Drop9thEmptyColumn(df)
#     df = MoveWithDrawalandDepositAmountToTransactionAmount(df)
#     df = CreateTransactionTypeColumn(df)
#     SaveToCSVFile(df, "C:/BigDataLocalSetup/spark/datasets/sample1Test")


# DoStep1(df)