Maya Playblast Tool
====
此工具用来创建Maya拍屏视频


### 使用要求
- 将程序包克隆到Maya可以导入位置。

- 必须安装Shuotgun RV，`并且购买正版License`，并在`blasterEnv.py`里配置RV的路径。

- 需要安装 `pillow` 和 `fire` 库。

- 开发人员需要使用 `_Compile_Exe.cmd` `把processor 编译成exe然后放到生产环境`，
  避免每台电脑安装python 和 依赖库。

- 生产环境内，`blasterEnv.py` 里的 第二个 `PROCESSOR`需要注释掉。




### 调用方法
```python
import blaster
blaster.UI()
```
