import datetime
from datetime import datetime, timedelta

maxWeek = 20; maxWeek += 1
classTime = [None, (8, 0), (8, 55), (10, 15), (11, 10), (14, 00), (14, 55), 
	(16, 15), (17, 10), (19, 0), (19, 55), (20, 50), (21, 45)]
weeks = [None]
starterDay = datetime(2020, 9, 7)
for i in range(1, maxWeek):
	singleWeek = [None]
	for d in range(0, 7):
		singleWeek.append(starterDay)
		starterDay = starterDay + timedelta(days = 1)
	weeks.append(singleWeek)

def oeWeek(startWeek, endWeek, mode):
	allWeek = range(startWeek, endWeek + 1)
	oddWeek = []; evenWeek = []
	for w in allWeek:
		if w % 2 == 0: evenWeek.append(w)
		else: oddWeek.append(w)
	if mode: return oddWeek
	else: return evenWeek

def rgWeek(startWeek, endWeek): return list(range(startWeek, endWeek + 1))


classes = [
	["大学物理A(下)", "刘俊(理)", "3507", "A15201A1110300012", rgWeek(1, 16), 1, [1, 2]],
	["随机数学(含概率论、数理 统计、随机过程)", "蒲兴成", "8141", "A15201A1110130006", rgWeek(1, 14), 1, [5, 6]],
	["电路理论及应用实验I(美方授课)", "杜佳佳", "电子技术实验室(一)(综合实验楼B201/B202)", "S15201A2021310001", rgWeek(2, 9), 2, [3, 4]],
	["微处理器(美方授课)", "Yangjie", "电子系统综合设计实验室2YF312", "AS15201A2011220001", rgWeek(1, 16), 2, rgWeek(5, 8)],
	["电路理论及应用I(美方授课)", "杜佳佳", "5404", "A15201A2021300001", rgWeek(1, 12), 3, rgWeek(1, 4)],
	["大学物理A(下)", "刘俊(理)", "3507", "A15201A1110300012", oeWeek(1, 15, 1), 3, [5, 6]],
	["大学物理实验A(下)", "李世⻓", "物理实验室(一)(综合实验楼C201/C202)", "S15201A2110680019", [1], 3, [9, 10]],
	["大学物理实验A(下)", "李世⻓", "光学设计性实验室(综合实验楼C312/C313)", "S15201A2110680019", [2, 13], 3, [9, 10]],
	["大学物理实验A(下)", "李世⻓", "电学设计性实验室(综合实验楼C310/C311)", "S15201A2110680019", [3], 3, [9, 10]],
	["大学物理实验A(下)", "李世⻓", "物理实验室(三)(综合实验楼C205)", "S15201A2110680019", [6], 3, [9, 10]],
	["大学物理实验A(下)", "李世⻓", "物理实验室(四)(综合实验楼C209/C210)", "S15201A2110680019", [8], 3, [9, 10]],
	["大学物理实验A(下)", "李世⻓", "物理实验室(二)(综合实验楼C203/C204)", "S15201A2110680019", [10], 3, [9, 10]],
	["大学物理实验A(下)", "李世⻓", "物理虚拟仿真实验室(综合实验楼C314/C315/C316)", "S15201A2110680019", [12], 3, [9, 10]],
	["随机数学(含概率论、数理 统计、随机过程)", "蒲兴成", "8141", "A15201A1110130006", rgWeek(1, 14), 4, [3, 4]],
	["中国近现代史纲要", "邓庆伟", "4509", "A15201A1100041008", rgWeek(1, 16), 4, [5, 6, 7]],
	["数学建模", "刘显全", "系统建模与仿真实验室SL110", "SK15201A2110910001", rgWeek(7, 14), 5, [1, 2]],
	["数学建模", "郑继明", "5200", "A15201A2110910001", rgWeek(1, 16), 5, [3, 4]],
	["大学生职业发展与就业指导1", "邹桦", "5401", "A15201B1220060061", rgWeek(1, 8), 5, [5, 6]]
]

iCalHeader = """BEGIN:VCALENDAR
METHOD:PUBLISH
VERSION:2.0
X-WR-CALNAME:课表
PRODID:-//Apple Inc.//Mac OS X 10.15.6//EN
X-WR-TIMEZONE:Asia/Shanghai
CALSCALE:GREGORIAN
BEGIN:VTIMEZONE
TZID:Asia/Shanghai
END:VTIMEZONE"""

createNow = datetime.now() - timedelta(hours = 8)
allvEvent = ""

for Class in classes:
	[Name, Teacher, Location, classID, classWeek, classWeekday, classOrder] = Class[:]
	Title = Name + " - " + Location

	if "YF" in Location: customGEO = """LOCATION:重庆邮电大学-逸夫科技楼\\n崇文路2号重庆邮电大学
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-APPLE-MAPKIT-HANDLE=;X-APPLE-RADIUS=200;X-TITLE=重庆邮电大学
 -逸夫科技楼\\\\n崇文路2号重庆邮电大学:geo:29.535617,106.607390"""

	if "SL" in Location: customGEO = """LOCATION:重庆邮电大学数理学院\\n崇文路2号重庆邮电大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-APPLE-MAPKIT-HANDLE=;X-APPLE-RADIUS=200;X-TITLE=重庆邮电大学
 数理学院\\\\n崇文路2号重庆邮电大学内:geo:29.530599,106.605454"""

	if "综合实验楼" in Location: customGEO = """LOCATION:重庆邮电大学综合实验大楼\\n南山路新力村
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-APPLE-MAPKIT-HANDLE=;X-APPLE-RADIUS=200;X-TITLE=重庆邮电大学
 综合实验大楼\\\\n南山路新力村:geo:29.524289,106.605595"""

	if Location[0] == "2": customGEO = """LOCATION:重庆邮电大学二教学楼\\n崇文路2号重庆邮电大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-APPLE-MAPKIT-HANDLE=;X-APPLE-RADIUS=200;X-TITLE=重庆邮电大学
 二教学楼\\\\n崇文路2号重庆邮电大学内:geo:29.532703,106.606747"""

	if Location[0] == "3": customGEO = """LOCATION:重庆邮电大学第三教学楼\\n崇文路2号
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-APPLE-MAPKIT-HANDLE=;X-APPLE-RADIUS=200;X-TITLE=重庆邮电大学
 第三教学楼\\\\n崇文路2号:geo:29.535119,106.609114"""

	if Location[0] == "4": customGEO = """LOCATION:重庆邮电大学第四教学楼\\n崇文路2号
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-APPLE-MAPKIT-HANDLE=;X-APPLE-RADIUS=200;X-TITLE=重庆邮电大学
 第四教学楼\\\\n崇文路2号:geo:29.536107,106.608759"""

	if Location[0] == "5": customGEO = """LOCATION:重庆邮电大学-国际学院\\n崇文路2号重庆邮电大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-APPLE-MAPKIT-HANDLE=;X-APPLE-RADIUS=200;X-TITLE=重庆邮电大学
 -国际学院\\\\n崇文路2号重庆邮电大学内:geo:29.536131,106.610090"""

	if Location[:2] == "81": customGEO = """LOCATION:重庆邮电大学八教学楼A栋\\n崇文路2号重庆邮电大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-APPLE-MAPKIT-HANDLE=;X-APPLE-RADIUS=200;X-TITLE=重庆邮电大学
 八教学楼A栋\\\\n崇文路2号重庆邮电大学内:geo:29.535322,106.611020"""

	if "运动场1" in Location: customGEO = """LOCATION:风华运动场\\n南山街道重庆邮电大学5栋
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-APPLE-MAPKIT-HANDLE=;X-APPLE-RADIUS=200;X-TITLE=
 风华运动场\\\\n南山街道重庆邮电大学5栋:geo:29.532757,106.607510"""

	for timeWeek in classWeek:
		classDate = weeks[timeWeek][classWeekday]
		startTime = classTime[classOrder[0]]; endTime = classTime[classOrder[-1]]
		classStartTime = classDate + timedelta(minutes = startTime[0] * 60 + startTime[1])
		classEndTime = classDate + timedelta(minutes = endTime[0] * 60 + endTime[1] + 45)
		Description = classID + " 任课教师: " + Teacher + "。"
		vEvent = "\nBEGIN:VEVENT"
		vEvent += "\nDTEND;TZID=Asia/Shanghai:" + classEndTime.strftime('%Y%m%dT%H%M%S')
		vEvent += "\nSUMMARY:" + Title
		vEvent += "\nDTSTART;TZID=Asia/Shanghai:" + classStartTime.strftime('%Y%m%dT%H%M%S')
		vEvent += "\nDESCRIPTION:" + Description
		vEvent += "\n" + customGEO
		vEvent += "\nEND:VEVENT"
		allvEvent += vEvent

allvEvent += "\nEND:VCALENDAR"

jWrite = open("cqupt_20201.ics", "w")
jWrite.write(iCalHeader + allvEvent)
jWrite.close()