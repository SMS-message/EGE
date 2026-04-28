from typing import TextIO


class MDParser(object):
    def __init__(self, md_file: TextIO):
        self.md_file = md_file

    def parse_md(self):
        parsed_string = self.match_markdown(self.md_file.read())
        with open("parsed_html.html", mode="w") as html:
            html.write(parsed_string)

    @staticmethod
    def match_markdown(string: str):
        lines = []
        for line in string.split("\n"):
            for sym in line:
                if line[:4] == " " * 4:
                    lines.append("<p class='space1'>{}</p>".format(line.strip()))
                    break
                match sym:
                    case "#":
                        lines.append("<h2>{}</h2>".format(line[1:].strip()))
                        break
            else:
                if not line:
                    lines.append("<br>")
                else:
                    lines.append("<p>{}</p>".format(line))
        return "\n".join(lines)
