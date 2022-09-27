## Python 大学生课表 (.ics) 生成

![效果图](render_2021.jpg)

此代码于 2021 年 3 月增加了日历项 UUID 生成，使得其更适合日历订阅，又于 2021 年 9 月修改了 UUID 生成方式，解决了随机 UUID 导致日历项重置的问题，敬请使用更新后的代码。2022 年 2 月，将数据输入和日历生成变得更为模块化，减少用户对主程序代码的修改，功能上与 2021 年 9 月发布的版本无异。

#### 已完成的一些学校项目

| 学校         | 项目地址                                            |
| ------------ | --------------------------------------------------- |
| 重庆邮电大学 | [CQUPT-ics](https://github.com/qwqVictor/CQUPT-ics) |
| 福建师范大学 | [FJNU-ics](https://github.com/payphone-x/FJNU-ics)  |



## 简介

iCalendar 是广泛使用的日历数据交换标准，在诸如 Apple 日历、Google Calendar 的日历 app 中创建日历项，不仅可清晰的了解日程安排，更可体验 iOS、Android 系统为日历提供的各种功能：计划出行时间、日程提醒、如 Siri 与 Google Assistant 等智能语音助理自动化服务等。

不过，并非所有学校都为学生提供 ics 日历，因此本代码旨在用 Python 3 协助你创建一个自己的基础 ics 日历课表。

**本代码的特色为：**

* 兼容 Apple 日历、Google Calendar、Outlook Calendar 等日历应用，**且支持上述应用的日历订阅**
* 支持多种课程时间安排：**单独的周数，范围的周数，奇偶周数**，如 "**第2周，5 至 11 周中的单数周，13 至 17 周**"
* 支持添加教学楼信息，其中 **Apple 日历还支持教学楼 Apple Maps 定位** ，在日历项中添加教学楼，就可在多个 iOS 地图等 app 中获得附加功能，如建议出发时间等
* 导入到系统日历后，支持诸多由操作系统提供的日历功能：例如，在 iOS 设备中添加日历项后，你可以直接向 Siri 询问：「我下周五有什么日程？」获得下周五的课表；或是在 Apple Watch 表盘上显示下一个课程的时间；或是使用 Shortcut 捷径进行更多操作

## 开始使用

库中共有三个代码：

* `timetable.py` 主函数
* `school.py` 一个包含课表 `classes` 和学校对象 `school` 的参考代码
* `CQUPT.py` 一个重庆邮电大学学生的实际课表和实际学校对象，作为示例

你只需要参考 `school.py` 编写一个属于自己学校和课表的代码即可！

### 建立你的 school.py

建议首先创建一个空白的代码，可复制 `school.py` 中的内容作为参考，例如命名为 MySchool.py。

#### 建立课程信息

在 `school.py` 中，有一个名为 `classes` 的数组，这是你填写课程的地方：

```python
classes = [
	["信号与系统", "张三", "5203", rgWeek(1, 12), 1, [3, 4]],
	# 信号与系统，张三老师，5203 教室，1 - 12 周，周一，3、4 节上课

	["面向对象程序设计", "李四", "综合实验楼B405", oeWeek(3, 17, 1), 3, [3, 4]],
	# 面向对象程序设计，李四老师，综合实验楼，3 - 17 周单周，周三，3、4 节上课

	["大学体育", "王五", "风华运动场", oeWeek(2, 16, 0), 3, [3, 4]],
	# 大学体育，王五老师，风华运动场，2 - 16 周双周，周三，3、4 节上课

	["马克思主义基本原理概论", "赵六", "3105", rgWeek(1, 8) + rgWeek(10, 16), 3, [5, 6, 7]],
	# 马克思主义基本原理概论，赵六老师，1 - 8 周及 10 - 16 周，周三，5、6、7 节上课
]
```

每一门课程都是一个数组，格式为 `[课程名, 教师名, 教室, 上课具体周, 周几, 第几节课]`

**如何设置课程在哪一周？**

单独周：请改为数组形式，例如 [2]；

范围周：可使用 `rgWeek` 函数，例如 `rgWeek(3, 7)` 代表第三周到第七周；

奇数周：可使用 `oeWeek` 函数，例如 `oeWeek(2, 9, 1)` 代表第二周到第九周的单数周，将 1 改为 0 即为偶数周。

**如何设置课程在哪一节？**
一节课：请改为数组形式，例如 [2]；

范围课，可使用 `rgWeek` 函数，例如 `rgWeek(3, 7)` 代表第三节一直上到第七节；

当然，在任意时候都可以直接用数组列举出所有的值，例如 `[2, 3, 5, 7, 10, 12, 16]`。如果周数、节数是由多项组成，请使用加法。例如，第2周，5-11单数周，13-17 周，则为：

```python
[2] + oeWeek(5, 11, 1) + rgWeek(13, 17)
```

#### 建立学校信息

```python
class school:
  name = "school"
  classTime = [(8, 0), (9, 0), (10, 0)]
  classPeriod = 50
  starterDay = [2022, 2, 28]
```

在 `school.py`，还有一个名为 `school` 的对象，这是你填写学校相关信息的地方：

* `classTime` 包含了每节课上课的时间点，用于生成每节课的具体日历项
* `classPeriod` 为每节课的时长
* `starterDay` 为开学第一周星期一的日期，作为生成日历的起始点

此外，还包装了  `geo`  函数和 `AppleMaps` 函数，可为你的日历项增加地点信息！详细的使用方法请参加下文的「为代码添加定位信息」段。

### 运行代码

在主函数  `timetable.py` 中的首几行：

```python
# 只需修改此处的导入文件名
from CQUPT import school, classes
```

修改 `CQUPT` 为你刚刚创建的代码名，例如：

```python
from MySchool import school, classes
```

然后运行即可！

## 生成后使用

* 要了解生成日历文件后如何导入或添加日历订阅到 Apple 设备，参阅[文档](https://github.com/qwqVictor/CQUPT-ics/blob/main/docs/ImportOrSubscribe.md)；
* 进阶使用：要了解什么是日历订阅，如何进行日历订阅，参阅[文档](https://github.com/qwqVictor/CQUPT-ics/blob/main/docs/ImportOrSubscribe.md)。

## 为代码添加定位信息

代码提供了两种添加定位信息的方法

* 方法一：将教室文字搭配坐标信息显示在日历中（几乎所有 ics 客户端都支持）

  ```python
  loc = "教室 " + classroom 
  cor = "30.0000;100.000"
  ```

  修改 `school` 对象中 `geo` 方法的 `loc` 和 `cor`，就可以根据教室返回特定的文字和坐标

* 方法二：使用 Apple Maps，添加教学楼的 GPS 坐标定位信息：

  Apple 日历使用了 `X-APPLE-STRUCTURED-LOCATION` 和 `X-APPLE-MAPKIT-HANDLE` 来记录 Apple Maps 位置信息，这一项包含位置文字和坐标，格式类似于下面的文段：

  ```C++
  LOCATION:重庆邮电大学综合实验大楼\n南山路新力村
  X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-APPLE-MAPKIT-HANDLE=;X-APPLE-RADIUS=500;X-TITLE=重庆邮电大学综合实验大楼\\n南山路新力村:geo:29.524289,106.605595
  ```

  其中，`LOCATION `和 `X-TITLE` 中的地址必须**一字不差**的和 Apple Maps 结果对应，方能保证其准确可用性。

  因此，建议通过在 macOS 上先手动创建日历项并提取系统创建的文本，以下是导出方法。

  * 打开 macOS 日历 app，任意创建一个日历项，添加你想要用在代码中的地理位置。

  * 请确定刚刚创建的日历项在哪一个日历里，然后点击 macOS 工具栏中的 文件 -> 导出 -> 导出，保存 ics 文件。

  * 用文本编辑器打开 ics 文件，找到一个由 `BEGIN:VEVENT` 开头的你刚刚建立的包含位置的 VEVENT 项目。

  * 你将可找到类似以下两个文段：

  ```C++
  LOCATION:重庆大学虎溪校区\n大学城南路55号  
  X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-APPLE-MAPKITHANDLE=1234567890ABCDEF;X-APPLE-RADIUS=925.4324489259043;X-TITLE=重庆大学虎溪校区\\n大学城南路5号:geo:29.592566,106.299150
  ```

  这里 `X-APPLE-MAPKITHANLE` 中的 `1234567890ABCDEF`  是一串随机文字，可以全部删除（注意不要删除后面的分号），`X-RADIUS` 无需修改，`X-TITLE` 请勿修改。

  在 `school.py` 的 `school` 对象中有匿名函数 `AppleMaps`，其本身将返回一个由字典组成的数组：

  ```python
  AppleMaps = lambda loc: [
    {
      "judge": "教学楼一" in loc,
      "text": r"""LOCATION:某大学一教学楼\n某大学内
  X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=某大学一教学楼\\n某大学内:geo:30.0000,100.000"""
    },
    {
      "judge": True,
      "text": r"""LOCATION:某大学一教学楼\n某大学内
  X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=某大学一教学楼\\n某大学内:geo:30.0000,100.000"""
    }
  ]
  ```
  
  每一个字典中，```judge``` 为匹配条件，只要可以作为 `if` 语句判断结果的均可作为条件，`text` 为刚刚获得的 Apple Maps 相关文本，这里使用了 r-String 和三引号文段便于你直接将 Apple Maps 生成的文本复制入内，而无需担心转义符号和换行符号的问题。最后确定 `geo` 方法中正确调用 Apple Maps 信息即可。
  


## 联系作者

* 直接提交 Issue
* 微博 [@赛艇的同学](http://weibo.com/u/3566216663 "@赛艇的同学")

