import datetime
from datetime import datetime, timedelta

maxWeek = 20; maxWeek += 1
classTime = [None, (8, 0), (8, 55), (10, 15), (11, 10), (14, 00), (14, 55), 
	(16, 15), (17, 10), (19, 0), (19, 55), (20, 50), (21, 45)]
weeks = [None]
starterDay = datetime(2019, 9, 2)
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
	["高等数学A(上)", "郑继明", "必修", "5.5", "3403", "A15191A1110010033", [2] + rgWeek(6, 18), 1, rgWeek(3, 4)],
	["C语言程序设计", "纪良浩", "必修", "3.0", "2117", "A15191A1040040010", [2] + rgWeek(7, 19), 1, rgWeek(5, 6)],
	["线性代数A", "张蓉", "必修", "3.0", "3401", "A15191A1110030014", [2] + rgWeek(6, 15), 2, rgWeek(1, 2)],
	["大学体育1-足球二班", "张文", "必修", "1.0", "运动场1", "A00191A1090010001", [2] + rgWeek(6, 19), 2, rgWeek(3, 4)],
	["综合英语1", "邱怡", "必修", "2.0", "5205", "A15191A2051090006", [2] + rgWeek(6, 19), 2, rgWeek(5, 6)],
	["托福A", "杨紫凌（外聘）", "选修", "6.0", "5305", "A15191A2150210002", [2] + rgWeek(6, 19), 2, rgWeek(9, 11)],
	["工程英语", "程方", "必修", "2.0", "5305", "A15191A2011200001", [2] + rgWeek(7, 19), 3, rgWeek(3, 4)],
	["高等数学A(上)", "郑继明", "必修", "5.5", "3403", "A15191A1110010033", [2] + rgWeek(6, 18), 3, rgWeek(7, 8)],
	["英语听说B", "Jones", "必修", "1.0", "5413", "A15191A2150041002", rgWeek(6, 13), 4, rgWeek(1, 2)],
	["C语言程序设计", "纪良浩", "必修", "0", "计算机教室（十三）(综合实验楼C410/C411) ", "SK15191A1040040021", oeWeek(7, 15, 1) + rgWeek(17, 19), 4, rgWeek(3, 4)],
	["线性代数A", "张蓉", "必修", "3.0", "3401", "A15191A1110030014", [2] + rgWeek(6, 15), 4, rgWeek(5, 6)],
	["托福A", "熊阳（外聘）", "选修", "6.0", "5305", "A15191A2150210002", [2] + rgWeek(6, 19), 4, rgWeek(9, 11)],
	["高等数学A(上)", "郑继明", "必修", "5.5", "3403", "A15191A1110010033", [2] + rgWeek(6, 17), 5, rgWeek(3, 4)],
	["健康教育1", "尹泽渊", "必修", "1.0", "5401", "A15191B1220040050", [12], 5, rgWeek(7, 8)],
	["健康教育1", "王军", "必修", "1.0", "5401", "A15191B1220040050", [11], 5, rgWeek(7, 8)],
	["健康教育1", "赵垚", "必修", "1.0", "5401", "A15191B1220040050", rgWeek(6, 10) + [13], 5, rgWeek(7, 8)]
]

iCalHeader = """BEGIN:VCALENDAR
METHOD:PUBLISH
VERSION:2.0
X-WR-CALNAME:课表
PRODID:-//Apple Inc.//Mac OS X 10.14.6//EN
X-WR-TIMEZONE:Asia/Shanghai
CALSCALE:GREGORIAN
BEGIN:VTIMEZONE
TZID:Asia/Shanghai
END:VTIMEZONE"""

createNow = datetime.now() - timedelta(hours = 8)
dtStamp = createNow.strftime('%Y%m%dT%H%M%SZ')

allvEvent = ""

for Class in classes:
	[Name, Teacher, Kind, Point, Location, classID, classWeek, classWeekday, classOrder] = Class[:]
	Title = Name + " - " + Location
	if "综合实验楼" in Location: customGEO = """LOCATION:重庆邮电大学综合实验大楼\\n南山路新力村
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-APPLE-MAPKIT-HANDLE=;X-APPLE-RADIUS=200;X-TITLE=重庆邮电大学
 综合实验大楼\\\\n南山路新力村:geo:29.524289,106.605595"""
	if Location[0] == "2": customGEO = """LOCATION:重庆邮电大学二教学楼\\n崇文路2号重庆邮电大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-APPLE-MAPKIT-HANDLE=;X-APPLE-RADIUS=200;X-TITLE=重庆邮电大学
 二教学楼\\\\n崇文路2号重庆邮电大学内:geo:29.532703,106.606747"""
	if Location[0] == "3": customGEO = """LOCATION:重庆邮电大学第三教学楼\\n崇文路2号
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-APPLE-MAPKIT-HANDLE=;X-APPLE-RADIUS=200;X-TITLE=重庆邮电大学
 第三教学楼\\\\n崇文路2号:geo:29.535119,106.609114"""
	if Location[0] == "5": customGEO = """LOCATION:重庆邮电大学-国际学院\\n崇文路2号重庆邮电大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-APPLE-MAPKIT-HANDLE=;X-APPLE-RADIUS=200;X-TITLE=重庆邮电大学
 -国际学院\\\\n崇文路2号重庆邮电大学内:geo:29.536131,106.610090"""
	if "运动场1" in Location: customGEO = """LOCATION:风华运动场\\n南山街道重庆邮电大学5栋
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-APPLE-MAPKIT-HANDLE=;X-APPLE-RADIUS=200;X-TITLE=
 风华运动场\\\\n南山街道重庆邮电大学5栋:geo:29.532757,106.607510"""
	Description = classID + " 任课教师: " + Teacher + "，该课程是" + Kind + "课，学分 " + Point + " 分。"
	classStartTime = []; classEndTime = []
	for timeWeek in classWeek:
		startTime = classTime[classOrder[0]]; endTime = classTime[classOrder[-1]]
		classStartTime.append(weeks[timeWeek][classWeekday] + timedelta(minutes = startTime[0] * 60 + startTime[1]))
		classEndTime.append(weeks[timeWeek][classWeekday] + timedelta(minutes = endTime[0] * 60 + endTime[1] + 45))
	for i in range(len(classStartTime)):
		vEvent = "\nBEGIN:VEVENT"
		vEvent += "\nDTEND;TZID=Asia/Shanghai:" + classEndTime[i].strftime('%Y%m%dT%H%M%S')
		vEvent += "\nSUMMARY:" + Title
		vEvent += "\nDTSTAMP:" + dtStamp
		vEvent += "\nDTSTART;TZID=Asia/Shanghai:" + classStartTime[i].strftime('%Y%m%dT%H%M%S')
		vEvent += "\nDESCRIPTION:" + Description
		vEvent += "\n" + customGEO
		vEvent += "\nEND:VEVENT"
		allvEvent += vEvent

jWrite = open("/Users/junyi_lou/Desktop/课表.ics", "w")
jWrite.write(iCalHeader + allvEvent + "\nEND:VCALENDAR")
jWrite.close(); exit()