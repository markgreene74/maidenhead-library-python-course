from csv import DictReader
from jinja2 import Template

DATA_CSV = "data/MOCK_DATA.csv"
TEMPLATE = "yaml/template.yaml.jinja"
OUTPUT = "yaml/output.yaml"

def extract_data(data_file) -> list[dict]:
    with open(data_file) as f:
        data = DictReader(f)
        rows = [row for row in data]

    return rows

def generate_yaml(data, template, output):
    with open(template) as f:
        jinja_template = f.read()

    template = Template(jinja_template)
    yaml_rendered = template.render(elements = data)

    with open(output, "w") as f:
        f.write(yaml_rendered)

if __name__ == "__main__":
    data = extract_data(DATA_CSV)
    generate_yaml(data, TEMPLATE, OUTPUT)
