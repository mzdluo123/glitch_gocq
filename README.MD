#glitch-gocq

在glitch平台上运行go-cqhttp，附带keeplive支持

# 使用步骤

1. 按照go-cqhttp的文档在你的电脑上运行go-cqhttp，并完成登录

    参考文档https://docs.go-cqhttp.org/guide/#go-cqhttp
2. 打开`config.yml`进行修改
   
    请注意，必须要将任何一个服务的端口改为`3000`,否则glitch无法识别，只能同时使用一个服务；
   例如开启正向ws之后就不能使用http。如果你使用的是反向ws，请再添加一个其他的正向服务来让glitch识别。
   
   我们强烈建议你设置一个api_token防止恶意访问

3. 导入项目到glitch
    在Glitch中创建一个新的项目，在左下角的tools里面找到导入，选择使用GitHub导入并输入本项目的名字`mzdluo123
/glitch_gocq`，即可导入
   
4. 传递配置文件

    打开 https://www.sojson.com/base64.html 将你的`config.yml`进行BASE64编码 ，在Glitch的左边栏找到`.env`，
   在里面新增一个叫做`CONF`的环境变量，将编码后的内容填进去。对`device.json`文件也需要使用相同的操作，对应的环境变量名称为`DEVICE`
   
5. 开始使用

   在左下角的tools内打开终端，敲`refresh`并回车即可使用