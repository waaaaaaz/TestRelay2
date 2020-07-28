## TestRelay2.0


## 需求
- 测试用例(测试脚本)及测试数据结构化
- 支持多种接口协议(目前支持http, 其他协议rpc, dubbo及mq等可扩展)
- 支持多种数据存储操作(目前支持mysql, mongodb, kafka)
- 用例设计基于端到端的测试场景, 基于测试数据断言; 移除通用断言避免, 类似"IS NOT NONE"的无效断言
- 易于平台化


## 安装
- python3最新版本
- pip install -r requirements.txt


## 用例编写
- 参考 [用例](test_suite)


## 执行
```bash
#查看帮助文档
python run.py --help
#运行
python run.py -P ./test_suite
```

## LICENSE
- MIT