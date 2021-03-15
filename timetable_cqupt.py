from random import sample
from datetime import datetime, timedelta

classTime = [None, (8, 0), (8, 55), (10, 15), (11, 10), (14, 00), (14, 55), 
	(16, 15), (17, 10), (19, 0), (19, 55), (20, 50), (21, 45)]
weeks = [None]
starterDay = datetime(2021, 3, 1)
for i in range(1, 30):
	singleWeek = [None]
	for d in range(0, 7):
		singleWeek.append(starterDay)
		starterDay += timedelta(days = 1)
	weeks.append(singleWeek)

oeWeek = lambda startWeek, endWeek, mode: [i for i in range(startWeek, endWeek + 1) if (i + mode) % 2 == 0]
rgWeek = lambda startWeek, endWeek: [i for i in range(startWeek, endWeek + 1)]
uid_generate = lambda: "-".join(map(lambda l: ''.join(sample("0123456789ABCDEF", l)), [8, 4, 4, 4, 12]))

classes = [
	["信号与系统（美方授课）", "廖莎莎", "5203", "A15202A2011290001", rgWeek(1, 12), 1, [3, 4]],
	["面向对象程序设计-JAVA", "唐晓军", "3106", "A15202A2040370002", rgWeek(1, 16), 1, [5, 6]],
	["信号与系统（美方授课）", "廖莎莎", "电子系统综合设计实验室2 YF312", "SK15202A2011290001", rgWeek(5, 12), 1, [9, 10]],
	["工程分析", "田娅", "5402", "A15202A2110660001", rgWeek(1, 16), 2, [1, 2]],
	["电子学导论(美方授课)", "杜佳佳", "5601", "A15202A2021320001", rgWeek(1, 12), 2, [5, 6]],
	["通信技术概论", "王毅", "2101", "R202A1015010001", rgWeek(1, 8), 2, [9, 10]],
	["信号与系统（美方授课）", "廖莎莎,Zhouxi", "5203", "A15202A2011290001", rgWeek(1, 12), 3, [1, 2]],
	["面向对象程序设计-JAVA", "唐晓军", "计算机教室（六）(综合实验楼B405/B406)", "SK15202A2040370003", oeWeek(3, 17, 1), 3, [3, 4]],
	["体育（俱乐部）-足球初级", "沈闯", "风华运动场01", "T00202A1090030012", oeWeek(2, 16, 0), 3, [3, 4]],
	["马克思主义基本原理概论", "李杨", "3105", "A15202A1100031016", rgWeek(1, 16), 3, [5, 6, 7]],
	["形势与政策", "曹华", "5401", "A15202A1100010015", rgWeek(5, 8), 4, [1, 2]],
	["健康教育2", "何雨桑", "5401", "A15202B1220050006", rgWeek(9, 16), 4, [1, 2]],
	["西方社会与文化", "tracy", "5405", "A15202A2150020002", rgWeek(1, 16), 4, [3, 4]],
	["工程分析", "田娅", "5402", "A15202A2110660001", rgWeek(1, 16), 4, [5, 6]],
	["电子学导论(美方授课)", "杜佳佳", "5601", "A15202A2021320001", rgWeek(1, 12), 4, [9, 10]],
	["电子学导论(美方授课)", "杜佳佳", "电子技术实验室（一）(综合实验楼B201/B202)", "SK15202A2021320001", rgWeek(2, 9), 5, [3, 4]]
]

iCal = """BEGIN:VCALENDAR
METHOD:PUBLISH
VERSION:2.0
X-WR-CALNAME:课表
PRODID:-//Apple Inc.//macOS 11.2.3//EN
X-APPLE-CALENDAR-COLOR:#711A76
X-WR-TIMEZONE:Asia/Shanghai
CALSCALE:GREGORIAN
BEGIN:VTIMEZONE
TZID:Asia/Shanghai
BEGIN:STANDARD
TZOFFSETFROM:+0900
RRULE:FREQ=YEARLY;UNTIL=19910914T170000Z;BYMONTH=9;BYDAY=3SU
DTSTART:19890917T020000
TZNAME:GMT+8
TZOFFSETTO:+0800
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETFROM:+0800
DTSTART:19910414T020000
TZNAME:GMT+8
TZOFFSETTO:+0900
RDATE:19910414T020000
END:DAYLIGHT
END:VTIMEZONE"""

runtime = datetime.now().strftime('%Y%m%dT%H%M%SZ')

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
	if "风华运动场" in Location: customGEO = """LOCATION:风华运动场\\n南山街道重庆邮电大学5栋
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-APPLE-MAPKIT-HANDLE=;X-APPLE-RADIUS=200;X-TITLE=
 风华运动场\\\\n南山街道重庆邮电大学5栋:geo:29.532757,106.607510"""

	for timeWeek in classWeek:
		classDate = weeks[timeWeek][classWeekday]
		startTime = classTime[classOrder[0]]; endTime = classTime[classOrder[-1]]
		classStartTime = classDate + timedelta(minutes = startTime[0] * 60 + startTime[1])
		classEndTime = classDate + timedelta(minutes = endTime[0] * 60 + endTime[1] + 45)
		Description = classID + " 任课教师: " + Teacher + "。"

		StartTime = classStartTime.strftime('%Y%m%dT%H%M%S')
		EndTime = classEndTime.strftime('%Y%m%dT%H%M%S')
		singleEvent = f"""
BEGIN:VEVENT
DTEND;TZID=Asia/Shanghai:{EndTime}
{customGEO}
DESCRIPTION:{Description}
UID:{uid_generate()}
DTSTAMP:{runtime}
URL;VALUE=URI:
X-APPLE-TRAVEL-ADVISORY-BEHAVIOR:AUTOMATIC
SUMMARY:{Title}
CREATED:{runtime}
DTSTART;TZID=Asia/Shanghai:{StartTime}
END:VEVENT"""
		iCal += singleEvent
iCal += "\nEND:VCALENDAR"

with open("cqupt.ics", "w", encoding = "utf-8") as w:
	w.write(iCal)