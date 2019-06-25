### 代码结构说明

1. 本项目代码为原项目https://github.com/XLab-Tongji/DizzyAI代码的重构，以后的更新将在本项目进行，原项目不再维护。

2. 各个字段提取函数已经分别封装在了不同的python文件中，命名格式为xxExtractor.py。 可以根据需要，以文件为粒度，增加不同的提取函数。

3. 任务类型以及其对应的提取函数君设计为可配置，配置信息写在mapping.json中。例如，如果我们需要在请假功能中祛除邮箱的提取，直接在"component"字段中删除“EmailExtractor”即可。 同理，如果我们希望增加一个提取的字段，直接在这里配置对应的Extractor即可。

4. 当前代码中已经没有任何硬编码的内容，从任务到提取函数均已经设计为可配置且动态插拔。

5. 核心设计思想为利用importlib工具实现python模块的动态加载。