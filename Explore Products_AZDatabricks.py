# Databricks notebook source
df1 = spark.read.format("csv").option("header", "true").load("dbfs:/FileStore/shared_uploads/ljmogashoa04@gmail.com/products.csv")

# COMMAND ----------

display(df1)

# COMMAND ----------

df1.write.saveAsTable("Products")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT ProductName, Category
# MAGIC From Products
# MAGIC WHERE Category = 'Road Bikes'
