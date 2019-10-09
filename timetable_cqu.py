import datetime
from datetime import datetime, timedelta

maxWeek = 20; maxWeek += 1
classTime = [None, (8, 30), (9, 20), (10, 30), (11, 20), (14, 00), (14, 50), 
	(16, 0), (16, 50), (19, 0), (19, 50), (20, 50)]
weeks = [None]
starterDay = datetime(2019, 9, 2)
for i in range(1, maxWeek):
	singleWeek = [None]
	for d in range(0, 7):
		singleWeek.append(starterDay)
		starterDay = starterDay + timedelta(days = 1)
	weeks.append(singleWeek)

def rgWeek(startWeek, endWeek): return list(range(startWeek, endWeek + 1))


classes = [
	["线性代数(II)", "[10010020]王克金", "010", "D1131", "MATH10032", rgWeek(6, 17), 1, rgWeek(1, 2)],
	["高等数学1(电子信息类)", "[10490018]罗广萍", "006", "D1234", "MATH10012", rgWeek(6, 18), 1, rgWeek(3, 4)],
	["计算机导论", "[18497016]刘凯", "002", "D1340", "CST11104", rgWeek(6, 17), 1, rgWeek(5, 6)],
	["形势与政策1", "[17497009]罗璇", "017", "DZ222", "MT80001", rgWeek(8, 11), 2, rgWeek(1, 2)],
	["程序设计基础(1)", "[18490041]陈波", "001", "D1151", "FCP0000", rgWeek(6, 17), 2, rgWeek(3, 4)],
	["中国近现代史纲要", "[01050010]孙青", "017", "D1231", "MT10200", rgWeek(6, 17), 2, rgWeek(5, 6)],
	["学业素养英语(2-1)", "[04030001]朱万忠", "087", "D1216", "EUS10022", rgWeek(6, 18), 2, rgWeek(7, 8)],
	["线性代数(II)", "[10010020]王克金", "010", "D1131", "MATH10032", rgWeek(6, 17), 3, rgWeek(1, 2)],
	["高等数学1(电子信息类)", "[10490018]罗广萍", "006", "D1234", "MATH10012", rgWeek(6, 18), 3, rgWeek(3, 4)],
	["中国近现代史纲要", "[01050010]孙青", "017", "D1231", "MT10200", rgWeek(6, 17), 4, rgWeek(1, 2)],
	["程序设计基础(1)", "[18490041]陈波", "001", "DYC303", "FCP0000", rgWeek(6, 9), 4, rgWeek(3, 4)],
	["计算机导论", "[18497016]刘凯", "002", "D1348", "CST11104", rgWeek(10, 13), 4, rgWeek(3, 4)],
	["高等数学1(电子信息类)", "[10490018]罗广萍", "006", "D1234", "MATH10012", rgWeek(6, 18), 5, rgWeek(3, 4)],
	["体育自选项目(太极养生)", "[25700108]涂毅", "008", "D东大门", "PESS22037", rgWeek(6, 18), 5, rgWeek(7, 8)],
	["新生研讨课", "[09000021]熊庆宇", "002", "D1251", "SE10001", rgWeek(6, 9), 6, rgWeek(1, 4)]
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
	[Name, Teacher, Classmates, Location, classID, classWeek, classWeekday, classOrder] = Class[:]
	Title = Name + " - " + Location
	if "D1" in Location: customGEO = """LOCATION:重庆大学虎溪校区第一教学楼\\n大学城南路55号重庆大学虎溪校区
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-APPLE-MAPKIT-HANDLE=;X-APPLE-RADIUS=337.55;X-TITLE=重庆大学虎溪校区
 第一教学楼\\""" + "\\n大学城南路55号重庆大学虎溪校区:geo:29.595578,106.301135"
	if "DZ" in Location: customGEO = """LOCATION:重庆大学虎溪校区综合楼\\n大学城南路55号重庆大学虎溪校区
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-APPLE-MAPKIT-HANDLE=;X-APPLE-RADIUS=340.61;X-TITLE=重庆大学虎溪校区
 综合楼\\""" + "\\n大学城南路55号重庆大学虎溪校区:geo:29.596055,106.299510"
	if "DYC" in Location: customGEO = """LOCATION:重庆大学虎溪校区艺术楼\\n大学城南路55号重庆大学虎溪校区
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-APPLE-MAPKIT-HANDLE=;X-APPLE-RADIUS=434.41;X-TITLE=重庆大学虎溪校区
 艺术楼\\""" + "\\n大学城南路55号重庆大学虎溪校区:geo:29.593464,106.304183"
	if "D东大门" in Location: customGEO = """LOCATION:重庆大学虎溪校区(东门)\\n虎溪镇
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-APPLE-MAPKIT-HANDLE=;X-APPLE-RADIUS=686.05;X-TITLE=重庆大学虎溪校区
 (东门)\\""" + "\\n虎溪镇:geo:29.594176,106.307050"
	Description = classID + " 教学班" + Classmates + " 任课教师" + Teacher + "。"
	classStartTime = []; classEndTime = []
	for timeWeek in classWeek:
		startTime = classTime[classOrder[0]]; endTime = classTime[classOrder[-1]]
		classStartTime.append(weeks[timeWeek][classWeekday] + timedelta(minutes = startTime[0] * 60 + startTime[1]))
		classEndTime.append(weeks[timeWeek][classWeekday] + timedelta(minutes = endTime[0] * 60 + endTime[1] + 50))
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