---
title: Hive使用笔记
date: 2017-03-01 20:02:07
tags:
---

Hive是Hadoop中一个类SQL的数据仓库。支持查询操作。
    

```
查看所有表
show tables;

修改hive表列的属性
alter table tablename change columnname1 columnname2 int;

查看表结构
desc tablename;

重命名
alter table source rename to target;

添加列
alter table target add columns (col3 string);

建表语句
CREATE EXTERNAL TABLE `tablename`(
      `s1` string,
      `s2` string,
      `s3` string)
    PARTITIONED BY (`date` string, 'scene' string)  //分区
    ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'  //以‘\t’分隔数据
    LOCATION '/home/mfcheer'                        //存储位置
```