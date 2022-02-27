# 一个重庆邮电大学的实现作为参考，代码不再包含任何其他注释

oeWeek = lambda startWeek, endWeek, mode: [i for i in range(startWeek, endWeek + 1) if (i + mode) % 2 == 0]
rgWeek = lambda startWeek, endWeek: [i for i in range(startWeek, endWeek + 1)]

classes = [
	["信号与系统", "张三", "5203", rgWeek(1, 12), 1, [3, 4]],
	["面向对象程序设计", "李四", "计算机教室（六）(综合实验楼B405/B406)", oeWeek(3, 17, 1), 3, [3, 4]],
	["大学体育", "王五", "风华运动场", oeWeek(2, 16, 0), 3, [3, 4]],
	["马克思主义基本原理概论", "赵六", "3105", rgWeek(1, 8) + rgWeek(10, 16), 3, [5, 6, 7]],
]

class school:

	name = "cqupt"

	classTime = [
		(8, 0), 
		(8, 55), 
		(10, 15), 
		(11, 10), 
		(14, 00), 
		(14, 55), 
		(16, 15), 
		(17, 10), 
		(19, 0), 
		(19, 55), 
		(20, 50), 
		(21, 45)
	]

	classPeriod = 45

	starterDay = [2022, 2, 28]

	AppleMaps = lambda loc: [
		{
			"judge": "YF" in loc,
			"text": r"""LOCATION:重庆邮电大学-逸夫科技楼\n崇文路2号重庆邮电大学
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学-逸夫科技楼\\n崇文路2号重庆邮电大学:geo:29.535617,106.607390"""
		},
		{
			"judge": "SL" in loc,
			"text": r"""LOCATION:重庆邮电大学数理学院\n崇文路2号重庆邮电大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学数理学院\\n崇文路2号重庆邮电大学内:geo:29.530599,106.605454"""
		},
		{
			"judge": ("风华" in loc) or (loc == "运动场1"),
			"text": r"""LOCATION:风华运动场\n南山街道重庆邮电大学5栋
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=风华运动场\\n南山街道重庆邮电大学5栋:geo:29.532757,106.607510"""
		},
		{
			"judge": "太极" in loc,
			"text": r"""LOCATION:重庆邮电大学-太极体育场\n崇文路2号重庆邮电大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学-太极体育场\\n崇文路2号重庆邮电大学内:geo:29.532940,106.609072"""
		},
		{
			"judge": "乒乓球" in loc,
			"text": r"""LOCATION:风雨操场(乒乓球馆)\n崇文路2号重庆邮电大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=风雨操场(乒乓球馆)\\n崇文路2号重庆邮电大学内:geo:29.534230,106.608516"""
		},
		{
			"judge": ("篮球" in loc) or ("排球" in loc),
			"text": r"""LOCATION:重庆邮电学院篮球排球馆\n崇文路2号重庆邮电大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电学院篮球排球馆\\n崇文路2号重庆邮电大学内:geo:29.534025,106.609148"""
		},
		{
			"judge": ("综合实验" in loc) or ("实验实训楼" in loc),
			"text": r"""LOCATION:重庆邮电大学综合实验大楼\n南山路新力村
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学综合实验大楼\\n南山路新力村:geo:29.524289,106.605595"""
		},
		{
			"judge": loc[0] == "1",
			"text": r"""LOCATION:重庆邮电大学-光电工程学院\n崇文路2号重庆邮电大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学-光电工程学院\\n崇文路2号重庆邮电大学内:geo:29.531478,106.605921"""
		},
		{
			"judge": loc[0] == "2",
			"text": r"""LOCATION:重庆邮电大学二教学楼\n崇文路2号重庆邮电大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学二教学楼\\n崇文路2号重庆邮电大学内:geo:29.532703,106.606747"""
		},
		{
			"judge": loc[0] == "3",
			"text": r"""LOCATION:重庆邮电大学第三教学楼\n崇文路2号
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学第三教学楼\\n崇文路2号:geo:29.535119,106.609114"""
		},
		{
			"judge": loc[0] == "4",
			"text": r"""LOCATION:重庆邮电大学第四教学楼\n崇文路2号
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学第四教学楼\\n崇文路2号:geo:29.536107,106.608759"""
		},
		{
			"judge": loc[0] == "5",
			"text": r"""LOCATION:重庆邮电大学-国际学院\n崇文路2号重庆邮电大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学-国际学院\\n崇文路2号重庆邮电大学内:geo:29.536131,106.610090"""
		},
		{
			"judge": loc[0] == "8",
			"text": r"""LOCATION:重庆邮电大学八教学楼A栋\n崇文路2号重庆邮电大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学八教学楼A栋\\n崇文路2号重庆邮电大学内:geo:29.535322,106.611020"""
		},
		{
			"judge": True,
			"text": r"""LOCATION:重庆邮电大学\n崇文路2号
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学\\n崇文路2号:geo:29.530807,106.607617"""
		}
	]

	def geo(classroom):
		loc = ""
		for place in school.AppleMaps(classroom):
			if place["judge"]:
				loc = place["text"]
				break
		return loc