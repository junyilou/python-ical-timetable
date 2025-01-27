import re
from dataclasses import dataclass
from datetime import datetime, timedelta
from hashlib import md5
from typing import Any


def EvenWeeks(start: int, end: int) -> list[int]:
    """
    返回偶数周列表
    如 even_week(1, 4) -> [2, 4]
    """
    return [i for i in range(start, end + 1) if not i % 2]

def OddWeeks(start: int, end: int) -> list[int]:
    """
    返回奇数周列表：
    如 odd_week(1, 4) -> [1, 3]
    """
    return [i for i in range(start, end + 1) if i % 2]

def Weeks(start: int, end: int) -> list[int]:
    """
    返回周数列表：
    如 week(1, 3) -> [1, 2, 3]
    """
    return list(range(start, end + 1))

@dataclass
class Course:
    name: str
    teacher: str
    classroom: str
    location: Any
    weekday: int
    weeks: list[int]
    indexes: list[int]

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

@dataclass
class School:
    duration: int
    timetable: list[tuple[int, int]]
    start: tuple[int, int, int]
    courses: list[Course]

    HEADERS = [
        "BEGIN:VCALENDAR",
        "METHOD:PUBLISH",
        "VERSION:2.0",
        "X-WR-CALNAME:课表",
        "X-WR-TIMEZONE:Asia/Shanghai",
        "CALSCALE:GREGORIAN",
        "BEGIN:VTIMEZONE",
        "TZID:Asia/Shanghai",
        "END:VTIMEZONE"]
    FOOTERS = ["END:VCALENDAR"]

    def __post_init__(self) -> None:
        assert self.timetable, "请设置每节课的上课时间，以 24 小时制两元素元组方式输入小时、分钟"
        assert len(self.start) >= 3, "请设置为开学第一周的日期，以元素元组方式输入年、月、日"
        assert self.courses, "请设置你的课表数组，每节课是一个 Course 实例"
        self.timetable.insert(0, (0, 0))
        self.start_dt = datetime(*self.start[:3])
        self.start_dt -= timedelta(days=self.start_dt.weekday())

    def time(self, week: int, weekday: int, index: int, plus: bool = False) -> datetime:
        """
        生成详细的日期和时间：
        week: 第几周，weekday: 周几，index: 第几节课，plus: 是否增加课程时间
        """
        date = self.start_dt + timedelta(weeks=week - 1, days=weekday - 1)
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
        coures = [
            [
                "BEGIN:VEVENT",
                f"SUMMARY:{course.title()}",
                f"DESCRIPTION:{course.description()}",
                f"DTSTART;TZID=Asia/Shanghai:{
                    self.time(week, course.weekday, course.indexes[0]):%Y%m%dT%H%M%S}",
                f"DTEND;TZID=Asia/Shanghai:{
                    self.time(week, course.weekday, course.indexes[-1], True):%Y%m%dT%H%M%S}",
                f"DTSTAMP:{runtime:%Y%m%dT%H%M%SZ}",
                f"UID:{md5(str((course.title, week, course.weekday,
                               course.indexes[0])).encode()).hexdigest()}",
                f"URL;VALUE=URI:",
                *course.location,
                "END:VEVENT",
            ]
            for course in self.courses
            for week in course.weeks
        ]
        items = [i for j in coures for i in j]
        for line in self.HEADERS + items + self.FOOTERS:
            first = True
            while line:
                texts.append((" " if not first else "") + line[:72])
                line = line[72:]
                first = False
        return "\n".join(texts)


@dataclass
class Geo:
    """
    仅提供坐标和地点名称的地点信息：
    name: 地点名称，lat：纬度，lon：经度
    """
    name: str
    lat: float | str
    lon: float | str

    @property
    def geo(self) -> str:
        return f"GEO:{self.lat};{self.lon}"

    def result(self) -> list[str]:
        return [f"LOCATION:{self.name}", self.geo]


class AppleMaps:
    """
    Apple Maps 地点信息：
    传入预先准备好的 ics 文件地址，自动分析
    """

    KEYS = ["SUMMARY", "LOCATION", "X-APPLE-STRUCTURED-LOCATION"]

    def __init__(self, calendar: str) -> None:
        self.locations: dict[str, dict[str, str]] = {}
        with open(calendar, encoding = "utf-8") as r:
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
        data = {k: next((i for i in lines if i.startswith(k)), "")
                for k in self.KEYS}
        if not all(data.values()):
            return
        title = data.pop("SUMMARY").removeprefix("SUMMARY:").strip()
        geo = re.findall(r"geo:([\d.]+),([\d.]+)",
                         data["X-APPLE-STRUCTURED-LOCATION"])
        if geo:
            data["GEO"] = Geo(title, geo[0][0], geo[0][1]).geo
        self.locations[title] = data

    def __getitem__(self, key: str) -> list[str]:
        try:
            return list(self.locations[key].values())
        except KeyError:
            ke = KeyError(f"没有找到 {key!r} 的 Apple Maps 信息")
            try:
                ke.add_note(f"已在日历文件中记录的地点有: {', '.join(self.locations)}")
            except AttributeError:
                pass
            raise ke from None
