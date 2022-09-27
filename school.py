# 编写你自己的学校对象和课表数据！

oeWeek = lambda startWeek, endWeek, mode: [i for i in range(startWeek, endWeek + 1) if (i + mode + 1) % 2] #奇偶周的实现函数
rgWeek = lambda startWeek, endWeek: [i for i in range(startWeek, endWeek + 1)] # 范围周的实现函数

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

class school:	

	name = "school"               # 学校的名称

	classTime = [
		(8, 0),
		(14, 10),
		(20, 20)
	]                             # 每节课的上课时间（如: 这 3 节课的上课时间分别是 上午 8:00、下午 2:10、晚上 8:20）

	classPeriod = 50              # 每一节课的时长分钟数（如: 50 分钟）

	starterDay = [2022, 2, 28]    # 开学第一周星期一的日期，存储为年、月、日三项

	AppleMaps = lambda loc: [     # （如果不使用 Apple Maps 可以完全忽略！）返回 Apple Maps 地址字典的匿名函数
		
		# 使用 r-String 以及三引号文段可以避免转义符号的歧义

		{
			"judge": "教学楼一" in loc,  # 设置匹配「教学楼一」的条件
			"text": r"""LOCATION:某大学一教学楼\n某大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=某大学一教学楼\\n某大学内:geo:30.0000,100.000"""  # 复制 Apple Maps 信息
		},
		{
			"judge": True,        # 请设置一个一直为 True 的建筑用于缺省匹配
			"text": r"""LOCATION:某大学一教学楼\n某大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=某大学一教学楼\\n某大学内:geo:30.0000,100.000"""
		}
	]

	def geo(classroom):

		# 方法零：完全不使用任何地理坐标信息（不建议）
		return ""

		# 方法一：将教室文字搭配坐标信息显示在日历中（几乎所有 ICS 客户端都支持）

		loc = "教室 " + classroom  # 想要显示在日历项地址中的文字
		cor = "30.0000;100.000"   # 地理坐标，纬度、经度之间以 ; 间隔
		return f"LOCATION:{loc}\nGEO:{cor}"  # 包装为符合 ICS 文件要求的格式

		# 方法二：使用 Apple Maps，匹配 `AppleMaps` 数组当中的场所

		loc = ""
		for place in school.AppleMaps(classroom):
			if place["judge"]:
				loc = place["text"]
				break
		return loc