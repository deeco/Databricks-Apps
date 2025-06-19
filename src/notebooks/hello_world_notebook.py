# Databricks notebook source
# MAGIC %md
# MAGIC # Hello World Job
# MAGIC 
# MAGIC This notebook is triggered by the Streamlit app and demonstrates a simple "Hello World" job.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Job Parameters
# MAGIC 
# MAGIC This job can accept parameters if needed.

# COMMAND ----------

# Get job parameters if any
dbutils.widgets.text("name", "World", "Name to greet")

name = dbutils.widgets.get("name")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Main Job Logic
# MAGIC 
# MAGIC This is where your actual job logic would go.

# COMMAND ----------

print(f"Hello, {name}!")
print(f"Job started at: {dbutils.notebook.entry_point.getDbutils().notebook().getContext().userName().get()}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Example: Simple Data Processing
# MAGIC 
# MAGIC Here's an example of how you might process some data:

# COMMAND ----------

# Create a simple DataFrame
from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp

spark = SparkSession.builder.appName("HelloWorldJob").getOrCreate()

# Create sample data
data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
df = spark.createDataFrame(data, ["name", "age"])

# Add timestamp
df_with_timestamp = df.withColumn("processed_at", current_timestamp())

# Show results
print("Processing complete!")
df_with_timestamp.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Job Completion
# MAGIC 
# MAGIC The job has completed successfully!

# COMMAND ----------

# Return success message
dbutils.notebook.exit("Job completed successfully!") 