import re
from datetime import datetime, timedelta
from hashlib import md5
from typing import Any


class Course:
    def __init__(
        self,
        name: str,
        teacher: str,
        classroom: str,
        location: Any,
        weekday: int,
        weeks: list[int],
        indexes: list[int],
    ) -> None:
        self.name = name
        self.teacher = teacher
        self.classroom = classroom
        self.location = location
        self.weekday = weekday
        self.weeks = weeks
        self.indexes = indexes

    def title(self) -> str:
        """
        每一次课程日历项的标题：
        如希望传递「当前是第几周」这样的参数，可在这里预留格式化变量，并在 School.generate() 函数中修改
        """
        return f"{self.name} - {self.classroom}"

    def description(self) -> str:
        """
        每一次课程日历项目的介绍信息：
        如希望传递「当前是第几周」这样的参数，可在这里预留格式化变量，并在 School.generate() 函数中修改
        """
        return f"任课教师：{self.teacher}。"

    @staticmethod
    def week(start: int, end: int) -> list[int]:
        """
        返回周数列表：
        如 week(1, 3) -> [1, 2, 3]
        """
        return list(range(start, end + 1))

    @staticmethod
    def odd_week(start: int, end: int) -> list[int]:
        """
        返回奇数周列表：
        如 odd_week(1, 4) -> [1, 3]
        """
        return [i for i in range(start, end + 1) if i % 2]

    @staticmethod
    def even_week(start: int, end: int) -> list[int]:
        """
        返回偶数周列表
        如 even_week(1, 4) -> [2, 4]
        """
        return [i for i in range(start, end + 1) if not i % 2]


class School:
    headers = [
        "BEGIN:VCALENDAR",
        "METHOD:PUBLISH",
        "VERSION:2.0",
        "X-WR-CALNAME:课表",
        "X-WR-TIMEZONE:Asia/Shanghai",
        "CALSCALE:GREGORIAN",
        "BEGIN:VTIMEZONE",
        "TZID:Asia/Shanghai",
        "END:VTIMEZONE",
    ]
    footers = ["END:VCALENDAR"]

    def __init__(
        self,
        duration: int = 45,
        timetable: list[tuple[int, int]] = [],
        start: tuple[int, int, int] = (2023, 9, 1),
        courses: list[Course] = [],
    ) -> None:
        assert timetable, "请设置每节课的上课时间，以 24 小时制两元素元组方式输入小时、分钟"
        assert len(start) == 3, "请设置为开学第一周的日期，以三元素元组方式输入年、月、日"
        assert courses, "请设置你的课表数组"
        self.duration = duration
        self.timetable = [[]] + timetable
        self.start: datetime = datetime(*start)
        while self.start.weekday():
            self.start -= timedelta(days=1)
        self.courses = courses

    def time(self, week: int, weekday: int, index: int, plus: bool = False) -> datetime:
        """
        生成详细的日期和时间：
        week: 第几周，weekday: 周几，index: 第几节课，plus: 是否增加课程时间
        """
        date = self.start + timedelta(weeks=week - 1, days=weekday - 1)
        return date.replace(
            hour=self.timetable[index][0], minute=self.timetable[index][1]
        ) + timedelta(minutes=self.duration if plus else 0)

    def generate(self) -> str:
        runtime = datetime.now()
        texts = []
        for course in self.courses:
            if not course.location:
                course.location = []
            elif isinstance(course.location, str):
                course.location = [f"LOCATION:{course.location}"]
            elif isinstance(course.location, Geo):
                course.location = course.location.result()
            assert isinstance(course.location, list), "课程定位信息类型不正确"
        items = [
            i
            for j in [
                [
                    "BEGIN:VEVENT",
                    f"SUMMARY:{course.title()}",
                    f"DESCRIPTION:{course.description()}",
                    f"DTSTART;TZID=Asia/Shanghai:{self.time(week, course.weekday, course.indexes[0]):%Y%m%dT%H%M%S}",
                    f"DTEND;TZID=Asia/Shanghai:{self.time(week, course.weekday, course.indexes[-1], True):%Y%m%dT%H%M%S}",
                    f"DTSTAMP:{runtime:%Y%m%dT%H%M%SZ}",
                    f"UID:{md5(str((course.title, week, course.weekday, course.indexes[0])).encode()).hexdigest()}",
                    f"URL;VALUE=URI:",
                    *course.location,
                    "END:VEVENT",
                ]
                for course in self.courses
                for week in course.weeks
            ]
            for i in j
        ]
        for line in self.headers + items + self.footers:
            first = True
            while line:
                texts.append((" " if not first else "") + line[:72])
                line = line[72:]
                first = False
        return "\n".join(texts)


class Geo:
    """
    仅提供坐标和地点名称的地点信息：
    name: 地点名称，lat：纬度，lon：经度
    """

    def __init__(self, name: str, lat: Any, lon: Any) -> None:
        self.loc = f"LOCATION:{name}"
        self.geo = f"GEO:{lat};{lon}"

    def result(self) -> list[str]:
        return [self.loc, self.geo]


class AppleMaps:
    """
    Apple Maps 地点信息：
    传入预先准备好的 ics 文件地址，自动分析
    """

    keys = ["SUMMARY", "LOCATION", "X-APPLE-STRUCTURED-LOCATION"]

    def __init__(self, calendar: str) -> None:
        self.locations: dict[str, dict[str, str]] = {}
        with open(calendar) as r:
            c = r.read()
        for i in re.findall(r"(?<=BEGIN:VEVENT)[\s\S]*?(?=END:VEVENT)", c):
            self.generate(i)

    def generate(self, event: str) -> None:
        lines = event.split("\n")
        for i, e in enumerate(lines):
            if not e.startswith(" "):
                continue
            d = i - 1
            while not lines[d]:
                d -= 1
            lines[d] += e.removeprefix(" ")
            lines[i] = ""
        data = {k: next((i for i in lines if i.startswith(k)), "") for k in self.keys}
        if not all(data.values()):
            return
        title = data.pop("SUMMARY").removeprefix("SUMMARY:").strip()
        geo = re.findall(r"geo:([\d.]+),([\d.]+)", data["X-APPLE-STRUCTURED-LOCATION"])
        if geo:
            data["GEO"] = Geo(title, geo[0][0], geo[0][1]).geo
        self.locations[title] = data

    def __getitem__(self, key: str) -> list[str]:
        try:
            assert key in self.locations, f"没有找到 {key!r} 的 Apple Maps 信息"
        except AssertionError as ae:
            try:
                ae.add_note(f"已在日历文件中记录的地点有: {', '.join(self.locations)}")
            except AttributeError:
                pass
            raise ae
        return list(self.locations[key].values())
