from csv import DictReader
from datetime import datetime as dt
from jinja2 import Template
from pathlib import Path

DATAFILE = Path("../data/course_dates.csv")
TEMPLATE = Path("../data/README.md.jinja")
README = Path("../README.md")


def read_csv(datafile: Path = DATAFILE) -> list[dict]:
    data = []
    with open(datafile) as csvfile:
        data_reader = DictReader(csvfile)
        data = [row for row in data_reader]

    # transform date from str into a native datetime
    for row in data:
        row["date"] = dt.fromisoformat(row["date"])

    data.sort(key=lambda x: (x["date"], x["time_start"]))
    return data


def write_readme(template_path: Path = TEMPLATE, readme_path: Path = README):
    course_dates = read_csv()
    course_dates_future = [row for row in course_dates if row["date"] >= dt.now()]
    course_dates_past = [row for row in course_dates if row["date"] < dt.now()]

    with open(template_path) as f:
        readme_jinja = f.read()

    template = Template(readme_jinja)
    readme_rendered = template.render(
        last_updated=str(dt.now().isoformat()),
        future_dates=course_dates_future,
        past_dates=course_dates_past,
    )

    with open(readme_path, "w") as f:
        f.write(readme_rendered)


if __name__ == "__main__":
    write_readme()
