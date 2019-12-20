import datetime
from datetime import datetime, timedelta

maxWeek = 20; maxWeek += 1
classTime = [None, (8, 0), (8, 55), (10, 15), (11, 10), (14, 00), (14, 55), 
	(16, 15), (17, 10), (19, 0), (19, 55), (20, 50), (21, 45)]
weeks = [None]
starterDay = datetime(2020, 2, 17)
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
	["高等数学A(下)", "郑继明", "5401", 5.5, "A15192A1110020040", rgWeek(1, 15), 1, [1, 2]],
	["形势与政策", "严常青", "5305", 0, "A15192A1100010064", rgWeek(5, 8), 1, [5, 6]],
	["数据结构与算法B", "黎贵友", "智能科学与技术实验室(综合实验楼B515)", 0, "SK15192A2040481001", rgWeek(9, 16), 1, [5, 6]],
	["思想政治理论课实践教学", "孙璐", "4212", 2, "S15192A1100060070", [2], 1, rgWeek(7, 8)],
	["大学物理实验A(上)", "虚拟教师", "物理实验室（一）(综合实验楼C201/C202)", 1, "S15192A2110670018", [12], 1, [9, 10]],
	["大学物理实验A(上)", "虚拟教师", "物理虚拟仿真实验室(综合实验楼C314/C315/C316)", 1, "S15192A2110670018", [9], 1, [9, 10]],
	["大学物理实验A(上)", "虚拟教师", "光学设计性实验室(综合实验楼C312/C313)", 1, "S15192A2110670018", [8], 1, [9, 10]],
	["大学物理实验A(上)", "虚拟教师", "电学设计性实验室(综合实验楼C310/C311)", 1, "S15192A2110670018", [6], 1, [9, 10]],
	["大学物理实验A(上)", "虚拟教师", "物理实验室（四）(综合实验楼C209/C210)", 1, "S15192A2110670018", [5], 1, [9, 10]],
	["大学物理实验A(上)", "虚拟教师", "物理实验室（二）(综合实验楼C203/C204)", 1, "S15192A2110670018", [1, 3, 14], 1, [9, 10]],
	["数字逻辑基础(美方授课)", "黄沛昱", "5203", 4, "A15192A2021330001", rgWeek(1, 12), 2, [9, 10]],
	["大学体育2-足球二班", "张文", "运动场1", 1, "A00192A1090020001", rgWeek(1, 16), 2, [5, 6]],
	["创新创业参赛执导（Mooc）", "彭语良", "3401", 1, "R192Mooc26002", [3, 10], 2, [11, 12]],
	["数字逻辑基础(美方授课)", "朱治国", "电子技术实验室（一）(综合实验楼B201/B202)", 0, "SK15192A2021330001", rgWeek(2, 9), 3, [3, 4]],
	["大学物理A(上)", "刘俊（理）", "5402", 3, "A15192A1110290011", rgWeek(1, 16), 3, [1, 2]],
	["高等数学A(下)", "郑继明", "5401", 5.5, "A15192A1110020040", rgWeek(1, 15), 3, [5, 6]],
	["数据结构与算法B", "张璞", "5200", 3, "A15192A2040481001", rgWeek(1, 16), 3, [9, 10]],
	["数字逻辑基础(美方授课)", "黄沛昱", "5203", 4, "A15192A2021330001", rgWeek(1, 12), 4, [1, 2]],
	["思想道德修养与法律基础", "张冬梅", "5305", 3, "A15192A1100021011", rgWeek(1, 16), 4, [5, 6, 7]],
	["高等数学A(下)", "郑继明", "5401", 5.5, "A15192A1110020040", rgWeek(1, 15), 5, [3, 4]],
	["大学物理A(上)", "刘俊（理）", "5402", 3, "A15192A1110290011", oeWeek(2, 16, 0), 5, [7, 8]]
]

iCalHeader = """BEGIN:VCALENDAR
METHOD:PUBLISH
VERSION:2.0
X-WR-CALNAME:课表
PRODID:-//Apple Inc.//Mac OS X 10.15.2//EN
X-WR-TIMEZONE:Asia/Shanghai
CALSCALE:GREGORIAN
BEGIN:VTIMEZONE
TZID:Asia/Shanghai
END:VTIMEZONE"""

createNow = datetime.now() - timedelta(hours = 8)
allvEvent = ""

for Class in classes:
	[Name, Teacher, Location, Score, classID, classWeek, classWeekday, classOrder] = Class[:]
	Title = Name + " - " + Location

	if "综合实验楼" in Location: customGEO = """LOCATION:重庆邮电大学综合实验大楼\\n南山路新力村
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-APPLE-MAPKIT-HANDLE=;X-APPLE-RADIUS=200;X-TITLE=重庆邮电大学
 综合实验大楼\\\\n南山路新力村:geo:29.524289,106.605595"""

	if Location[0] == "4": customGEO = """LOCATION:重庆邮电大学第四教学楼\\n崇文路2号
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-APPLE-MAPKIT-HANDLE=;X-APPLE-RADIUS=200;X-TITLE=重庆邮电大学
 第四教学楼\\\\n崇文路2号:geo:29.536107,106.608759"""

	if Location[0] == "5": customGEO = """LOCATION:重庆邮电大学-国际学院\\n崇文路2号重庆邮电大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-APPLE-MAPKIT-HANDLE=;X-APPLE-RADIUS=200;X-TITLE=重庆邮电大学
 -国际学院\\\\n崇文路2号重庆邮电大学内:geo:29.536131,106.610090"""

	if "运动场1" in Location: customGEO = """LOCATION:风华运动场\\n南山街道重庆邮电大学5栋
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-APPLE-MAPKIT-HANDLE=;X-APPLE-RADIUS=200;X-TITLE=
 风华运动场\\\\n南山街道重庆邮电大学5栋:geo:29.532757,106.607510"""

	
	for timeWeek in classWeek:
		classDate = weeks[timeWeek][classWeekday]
		startTime = classTime[classOrder[0]]; endTime = classTime[classOrder[-1]]
		classStartTime = classDate + timedelta(minutes = startTime[0] * 60 + startTime[1])
		classEndTime = classDate + timedelta(minutes = endTime[0] * 60 + endTime[1] + 45)
		Description = classID + " 任课教师: " + Teacher + "，学分 " + str(Score) + " 分。"
		vEvent = "\nBEGIN:VEVENT"
		vEvent += "\nDTEND;TZID=Asia/Shanghai:" + classEndTime.strftime('%Y%m%dT%H%M%S')
		vEvent += "\nSUMMARY:" + Title
		vEvent += "\nDTSTART;TZID=Asia/Shanghai:" + classStartTime.strftime('%Y%m%dT%H%M%S')
		vEvent += "\nDESCRIPTION:" + Description
		vEvent += "\n" + customGEO
		vEvent += "\nEND:VEVENT"
		allvEvent += vEvent

allvEvent += "\nEND:VCALENDAR"

jWrite = open("/Users/junyi_lou/Desktop/cqupt_2020.ics", "w")
jWrite.write(iCalHeader + allvEvent)
jWrite.close(); exit()