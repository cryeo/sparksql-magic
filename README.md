# sparksql-magic

Spark SQL magic command for Jupyter notebooks.

![Example](screenshots/example.png)

## Prerequisites
- Python >= 3.6
- PySpark >= 2.3.0
- IPython >= 7.4.0

## Install
```
pip install sparksql-magic
```

## Usage

### Load
```
%load_ext sparksql_magic
```

### Config
```
%config SparkSql.limit=<INT>
```

|Option|Default|Description|
|---|---|---|
|`SparkSql.limit`|20|The maximum number of rows to display|

### Parameter
```
%%sparksql [-c|--cache] [-e|--eager] [-v|--view VIEW] [-l|--limit LIMIT] [variable]
<QUERY>
```

|Parameter|Description|
|---|---|
|`-c` `--cache`|Cache dataframe|
|`-e` `--eager`|Cache dataframe with eager load|
|`-v VIEW` `--view VIEW`|Create or replace temporary view|
|`-l LIMIT` `--limit LIMIT`|The maximum number of rows to display (Default: `SparkSql.limit`)|
|`variable`|Capture dataframe in a local variable|



