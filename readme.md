#### 安装
1. 基础依赖安装使用pip install即可，例如nltk, jieba等，根据运行提示安装缺少的依赖。

2. 对于standford coreNLP的安装，首先下载 http://nlp.stanford.edu/software/stanford-corenlp-full-2018-10-05.zip 并解压缩，然后下载 http://nlp.stanford.edu/software/stanford-chinese-corenlp-2018-10-05-models.jar 中文扩展，并将此jar包放入解压缩的文件夹内。最后在main.py中206行的文件夹地址改为解压缩的地址即可。

3. 根据项目的readme文件，安装https://github.com/Ryaninf/Time-NLPY/blob/master/README.md。

#### 启动方式：

Pycharm打开项目后，运行LoadProperty.py文件。

#### 特殊提示：
1.审批人配置在resource/myDict.dict中，姓名可以模糊匹配。

2.请假时间三个要素：开始时间、时长、结束时间，三个必须满足两个。时长最小单位可以为半天。

3.请假理由一般为动宾短语或是整句，有时会出现bug，可以记录并反馈。

4.邮箱格式必须满足 xx@xx.xx 。

5.最后提示是否确认，若不确认将会清空。

#### 测试用例：
1. 我要请假去看病，让杨慧宇帮我批一下，从明天到周五。

2. 你好，我想请个事假，我要去开家长会。六月十八号下午请半天假。

3. 我想请个假。

   后天起请三天假。
   
   杨慧禹
   
### 代码说明：

1. 本项目代码为原项目 https://github.com/XLab-Tongji/DizzyAI 代码的重构，以后的更新将在本项目进行，原项目不再维护。

2. 各个字段提取函数已经分别封装在了不同的python文件中，命名格式为xxExtractor.py。 可以根据需要，以文件为粒度，增加不同的提取函数。

3. 任务类型以及其对应的提取函数君设计为可配置，配置信息写在mapping.json中。例如，如果我们需要在请假功能中祛除邮箱的提取，直接在"component"字段中删除“EmailExtractor”即可。 同理，如果我们希望增加一个提取的字段，直接在这里配置对应的Extractor即可。

4. 当前代码中已经没有任何硬编码的内容，从任务到提取函数均已经设计为可配置且动态插拔。

5. 核心设计思想为利用importlib工具实现python模块的动态加载。   
