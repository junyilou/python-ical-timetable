# 重庆文理学院

oeWeek = lambda startWeek, endWeek, mode: [i for i in range(startWeek, endWeek + 1) if (i + mode) % 2 == 0] 
rgWeek = lambda startWeek, endWeek: [i for i in range(startWeek, endWeek + 1)] 

classes = [
	["信号与系统", "张三", "5203", rgWeek(1, 12), 1, [3, 4]],
	["面向对象程序设计", "李四", "计算机教室（六）(综合实验楼B405/B406)", oeWeek(3, 17, 1), 3, [3, 4]],
	["大学体育", "王五", "风华运动场", oeWeek(2, 16, 0), 3, [3, 4]],
	["马克思主义基本原理概论", "赵六", "3105", rgWeek(1, 8) + rgWeek(10, 16), 3, [5, 6, 7]],
]

class school:	

	name = "CQWU"               

	classTime = [
		(8, 10),
		(9, 5),
		(10, 20),
		(11, 15),
		(14, 30),
		(15, 25),
		(16, 20),
		(17, 15),
		(19, 20),
		(20, 15),
		(21, 10)
	]                             

	classPeriod = 45              

	starterDay = [2022, 9, 5]    

	AppleMaps = lambda loc: []

	def geo(classroom):
		loc = "教室 " + classroom  
		cor = "29.351342, 105.938361"   
		return f"LOCATION:{loc}\nGEO:{cor}"  
