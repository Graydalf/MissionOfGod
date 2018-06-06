训练集  train.tree
测试集  test.sent

你可以再将训练集拆分成训练集和开发集，但是训练过程中不允许使用测试集。

作业文件列表

----学号_姓名_第二次作业
---------pcfg.py
---------train.tree (可选)
---------test.sent (可选)
---------output.tree


训练集只允许使用train.tree,不允许使用其他资料
测试集只允许使用test.sent, 不允许使用其他资料, 这是带词性的句子的原型，需要你分析为树状结构，格式应当和 test.tree一致。

助教执行如下命令
python pcfg.py train
python pcfg.py test

50分和0分标准同上次作业。