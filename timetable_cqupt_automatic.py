import datetime, requests, json
from datetime import datetime, timedelta

maxWeek = 20; maxWeek += 1
classTime = [None, (8, 0), (8, 55), (10, 15), (11, 10), (14, 00), (14, 55), 
	(16, 15), (17, 10), (19, 0), (19, 55), (20, 50), (21, 45)]
weeks = [None]
starterDay = datetime(2019, 9, 2)
for i in range(1, maxWeek):
	singleWeek = []
	for d in range(0, 7):
		singleWeek.append(starterDay)
		starterDay = starterDay + timedelta(days = 1)
	weeks.append(singleWeek)

def kebiao(studentNum):
	data = {"stuNum": studentNum}; kecheng = []
	headers = {"User-Agent": "zhang shang zhong you/4.0.6 (iPhone; iOS 13.2.2; Scale/2.00)"}
	try: r = requests.post(url = 'https://cyxbsmobile.redrock.team/api/kebiao', data = data, headers = headers, timeout = 10)
	except: return "Request Timeout"
	ansTable = json.loads(r.text)["data"]
	for _Class in ansTable:
		kecheng.append(["CLASS", _Class["course"], _Class["teacher"], _Class["type"], _Class["rawWeek"], _Class["classroom"], 
			_Class["course_num"], _Class["week"], _Class["hash_day"], [_Class["begin_lesson"], _Class["begin_lesson"] + _Class["period"] - 1]])
	return kecheng

def kaoshi(studentNum):
	data = {"stuNum": studentNum}; tests = []
	headers = {"User-Agent": "zhang shang zhong you/4.0.6 (iPhone; iOS 13.2.2; Scale/2.00)"}
	try: r = requests.post(url = 'https://cyxbsmobile.redrock.team/api/examSchedule', data = data, headers = headers, timeout = 10)
	except: return "Request Timeout"
	ansTable = json.loads(r.text)["data"]
	for _Test in ansTable:
		tests.append(["TEST", _Test["course"], _Test["begin_time"], _Test["end_time"], "", _Test["classroom"], 
			"", [int(_Test["week"])], int(_Test["weekday"]) - 1, _Test["seat"]])
	return tests

studentNum = 2017212136
classes = kebiao(studentNum) + kaoshi(studentNum)

iCalHeader = """BEGIN:VCALENDAR
METHOD:PUBLISH
VERSION:2.0
X-WR-CALNAME:课表
PRODID:-//Apple Inc.//Mac OS X 10.15.1//EN
X-WR-TIMEZONE:Asia/Shanghai
CALSCALE:GREGORIAN
BEGIN:VTIMEZONE
TZID:Asia/Shanghai
END:VTIMEZONE"""

createNow = datetime.now() - timedelta(hours = 8)
dtStamp = createNow.strftime('%Y%m%dT%H%M%SZ')

allvEvent = ""

for __Class in classes:
	customGEO = ""
	[CID, Name, Teacher, Kind, RawWeek, Location, classID, classWeek, classWeekday, classOrder] = __Class

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

	if Location[0] == "8": customGEO = """LOCATION:重庆邮电大学八教学楼A栋\\n崇文路2号重庆邮电大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-APPLE-MAPKIT-HANDLE=;X-APPLE-RADIUS=200;X-TITLE=重庆邮电大学
 八教学楼A栋\\\\n崇文路2号重庆邮电大学内:geo:29.535322,106.611020"""

	if "运动场1" in Location: customGEO = """LOCATION:风华运动场\\n南山街道重庆邮电大学5栋
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-APPLE-MAPKIT-HANDLE=;X-APPLE-RADIUS=200;X-TITLE=
 风华运动场\\\\n南山街道重庆邮电大学5栋:geo:29.532757,106.607510"""

	for timeWeek in classWeek:
		classDate = weeks[timeWeek][classWeekday]
		if CID == "CLASS":
			startTime = classTime[classOrder[0]]; endTime = classTime[classOrder[-1]]
			classStartTime = classDate + timedelta(minutes = startTime[0] * 60 + startTime[1])
			classEndTime = classDate + timedelta(minutes = endTime[0] * 60 + endTime[1] + 45)
			Title = Name + " - " + Location
			Description = (classID + " 任课教师: " + Teacher + "，该课程是" + Kind + "课，在" + 
				RawWeek.replace(",", "、") + "行课，当前是第" + str(timeWeek) + "周。")
		if CID == "TEST":
			startTime = Teacher.split(":"); endTime = Kind.split(":")
			classStartTime = classDate + timedelta(minutes = int(startTime[0]) * 60 + int(startTime[1]))
			classEndTime = classDate + timedelta(minutes = int(endTime[0]) * 60 + int(endTime[1]))
			Title = "[考试] " + Name + " - " + Location
			Description = ("考试在第" + str(timeWeek) + "周进行，时间为" + Teacher + "至" + Kind +
				"，考试座位号是" + classOrder + "，祝考试顺利！")
		vEvent = "\nBEGIN:VEVENT"
		vEvent += "\nDTEND;TZID=Asia/Shanghai:" + classEndTime.strftime('%Y%m%dT%H%M%S')
		vEvent += "\nSUMMARY:" + Title
		vEvent += "\nDTSTAMP:" + dtStamp
		vEvent += "\nDTSTART;TZID=Asia/Shanghai:" + classStartTime.strftime('%Y%m%dT%H%M%S')
		vEvent += "\nDESCRIPTION:" + Description
		vEvent += "\n" + customGEO
		vEvent += "\nEND:VEVENT"
		allvEvent += vEvent

allvEvent += "\nEND:VCALENDAR"

jWrite = open("/root/www/cqupt.ics", "w")
jWrite.write(iCalHeader + allvEvent); jWrite.close()