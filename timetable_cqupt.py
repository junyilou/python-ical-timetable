from hashlib import md5
from datetime import datetime, timedelta

classTime = [None, (8, 0), (8, 55), (10, 15), (11, 10), (14, 00), (14, 55), 
	(16, 15), (17, 10), (19, 0), (19, 55), (20, 50), (21, 45)]
weeks = [None]
starterDay = datetime(2021, 9, 6)
for i in range(1, 30):
	singleWeek = [None]
	for d in range(0, 7):
		singleWeek.append(starterDay)
		starterDay += timedelta(days = 1)
	weeks.append(singleWeek)

oeWeek = lambda startWeek, endWeek, mode: [i for i in range(startWeek, endWeek + 1) if (i + mode) % 2 == 0]
rgWeek = lambda startWeek, endWeek: [i for i in range(startWeek, endWeek + 1)]
uid_generate = lambda key1, key2: md5(f"{key1}{key2}".encode("utf-8")).hexdigest()

classes = [
	["信号与系统", "张三", "5203", "A15202A2011290001", rgWeek(1, 12), 1, [3, 4]],
	# 信号与系统，张三老师，5203 教室，1 - 12 周，周一，3、4 节上课
	["面向对象程序设计", "李四", "计算机教室（六）(综合实验楼B405/B406)", "SK15202A2040370003", oeWeek(3, 17, 1), 3, [3, 4]],
	# 面向对象程序设计，李四老师，综合实验楼，3 - 17 周单周，周三，3、4 节上课
	["大学体育", "王五", "风华运动场", "T00202A1090030012", oeWeek(2, 16, 0), 3, [3, 4]],
	# 大学体育，王五老师，风华运动场，2 - 16 周双周，周三，3、4 节上课
	["马克思主义基本原理概论", "赵六", "3105", "A15202A1100031016", rgWeek(1, 8) + rgWeek(10, 16), 3, [5, 6, 7]],
	# 马克思主义基本原理概论，赵六老师，1 - 8 周及 10 - 16 周，周三，5、6、7 节上课
]

iCal = """BEGIN:VCALENDAR
METHOD:PUBLISH
VERSION:2.0
X-WR-CALNAME:课表
X-WR-TIMEZONE:Asia/Shanghai
CALSCALE:GREGORIAN
BEGIN:VTIMEZONE
TZID:Asia/Shanghai
END:VTIMEZONE
"""

def get_location(loc):
	from re import search
	try:
		room = search("[0-9]{4}", loc).group()
	except AttributeError:
		room = "6666"
	if "YF" in loc: 
		customGEO = """LOCATION:重庆邮电大学-逸夫科技楼\\n崇文路2号重庆邮电大学
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学
 -逸夫科技楼\\\\n崇文路2号重庆邮电大学:geo:29.535617,106.607390"""
	elif "SL" in loc: 
		customGEO = """LOCATION:重庆邮电大学数理学院\\n崇文路2号重庆邮电大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学
 数理学院\\\\n崇文路2号重庆邮电大学内:geo:29.530599,106.605454"""
	elif "综合实验" in loc or "实验实训室" in loc: 
		customGEO = """LOCATION:重庆邮电大学综合实验大楼\\n南山路新力村
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学
 综合实验大楼\\\\n南山路新力村:geo:29.524289,106.605595"""
	elif "风华" in loc or loc == "运动场1": 
		customGEO = """LOCATION:风华运动场\\n南山街道重庆邮电大学5栋
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=
 风华运动场\\\\n南山街道重庆邮电大学5栋:geo:29.532757,106.607510"""
	elif "太极" in loc:
		customGEO = """LOCATION:重庆邮电大学-太极体育场\\n崇文路2号重庆邮电大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学
 -太极体育场\\\\n崇文路2号重庆邮电大学内:geo:29.532940,106.609072"""
	elif "乒乓球" in loc:
		customGEO = """LOCATION:风雨操场(乒乓球馆)\\n崇文路2号重庆邮电大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=风雨操场(乒乓球馆)\\\\n
 崇文路2号重庆邮电大学内:geo:29.534230,106.608516"""
	elif "篮球" in loc or "排球" in loc:
		customGEO = """LOCATION:重庆邮电学院篮球排球馆\\n崇文路2号重庆邮电大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电学院篮球排球馆\\\\n
 崇文路2号重庆邮电大学内:geo:29.534025,106.609148"""
	elif room[0] == "1":
		customGEO = """LOCATION:重庆邮电大学-光电工程学院\\n崇文路2号重庆邮电大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学
 -光电工程学院\\\\n崇文路2号重庆邮电大学内:geo:29.531478,106.605921"""
	elif room[0] == "2": 
		customGEO = """LOCATION:重庆邮电大学二教学楼\\n崇文路2号重庆邮电大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学
 二教学楼\\\\n崇文路2号重庆邮电大学内:geo:29.532703,106.606747"""
	elif room[0] == "3": 
		customGEO = """LOCATION:重庆邮电大学第三教学楼\\n崇文路2号
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学
 第三教学楼\\\\n崇文路2号:geo:29.535119,106.609114"""
	elif room[0] == "4": 
		customGEO = """LOCATION:重庆邮电大学第四教学楼\\n崇文路2号
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学
 第四教学楼\\\\n崇文路2号:geo:29.536107,106.608759"""
	elif room[0] == "5": 
		customGEO = """LOCATION:重庆邮电大学-国际学院\\n崇文路2号重庆邮电大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学
 -国际学院\\\\n崇文路2号重庆邮电大学内:geo:29.536131,106.610090"""
	elif room[0] == "8": 
		customGEO = """LOCATION:重庆邮电大学八教学楼A栋\\n崇文路2号重庆邮电大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学
 八教学楼A栋\\\\n崇文路2号重庆邮电大学内:geo:29.535322,106.611020"""
	else: #Fallback
		customGEO = """LOCATION:重庆邮电大学\\n崇文路2号
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=
 重庆邮电大学\\\\n崇文路2号:geo:29.530807,106.607617"""
	customGEO = f'\n{customGEO}\nGEO:{customGEO.split("geo:")[1].replace(",", ";")}'
	return customGEO

runtime = datetime.now().strftime('%Y%m%dT%H%M%SZ')

for Class in classes:
	[Name, Teacher, Location, classID, classWeek, classWeekday, classOrder] = Class[:]
	Title = Name + " - " + Location
	
	customGEO = get_location(Location) # 通过 geo_location 匹配，也可替换为其他文本

	for timeWeek in classWeek:
		classDate = weeks[timeWeek][classWeekday]
		startTime = classTime[classOrder[0]]; endTime = classTime[classOrder[-1]]
		classStartTime = classDate + timedelta(minutes = startTime[0] * 60 + startTime[1])
		classEndTime = classDate + timedelta(minutes = endTime[0] * 60 + endTime[1] + 45)
		Description = classID + " 任课教师: " + Teacher + "。"

		StartTime = classStartTime.strftime('%Y%m%dT%H%M%S')
		EndTime = classEndTime.strftime('%Y%m%dT%H%M%S')
		singleEvent = f"""BEGIN:VEVENT
DTEND;TZID=Asia/Shanghai:{EndTime}
DESCRIPTION:{Description}
UID:CQUPT-{uid_generate(Name, StartTime)}
DTSTAMP:{runtime}
URL;VALUE=URI:{customGEO}
SUMMARY:{Title}
DTSTART;TZID=Asia/Shanghai:{StartTime}
END:VEVENT
"""
		iCal += singleEvent

iCal += "END:VCALENDAR"

with open("cqupt.ics", "w", encoding = "utf-8") as w:
	w.write(iCal)