# 美赛中使用的爬虫代码，用于爬取语言数据网站中的数据

## language.py

根据语言的ISO标准码，爬取选定的语言信息其网页表格中population一行的信息。

输出为output - 17.csv，17是代码中27行flag=17确定的，代表读取的版本号

## country-e.py

最早准备爬取所有语言的信息，使用country.py，修改里面第8行flag='e'作为读取以E为开头索引的语言，本准备生成这样a-z所有文件同时跑来爬取，因队伍决策中断，这里'e'为其中一个修改flag后的文件，爬取结果为output-e.csv