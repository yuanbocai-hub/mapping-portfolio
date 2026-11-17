"""Make an offline browsing copy; preserve existing GitHub links to map masters."""
from pathlib import Path
import base64
import mimetypes
import re
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = "https://github.com/yuanbocai-hub/crooked-stern-junk/raw/refs/heads/main/"


def data_url(path):
    mime = mimetypes.guess_type(str(path))[0] or "application/octet-stream"
    return "data:" + mime + ";base64," + base64.b64encode(path.read_bytes()).decode()


def build():
    page = (ROOT / "index.html").read_text()
    page = page.replace('<link rel="stylesheet" href="portfolio.css">',
                        "<style>" + (ROOT / "portfolio.css").read_text() + "</style>")
    page = page.replace('<script src="portfolio.js" defer></script>', "")
    page = page.replace("<body>", '<body data-preview-mode>')
    page = page.replace("</body>", "<script>" + (ROOT / "portfolio.js").read_text() + "</script></body>")
    page = re.sub(r'src="(assets/[^\"]+)"',
                  lambda match: 'src="' + data_url(ROOT / match.group(1)) + '"', page)

    def replace_link(match):
        path = match.group(1)
        if not (ROOT / path).is_file():
            return match.group(0)
        if path.startswith("assets/figures/"):
            target = data_url(ROOT / "assets" / (Path(path).stem + ".jpg"))
        else:
            target = PUBLIC + quote(path)
        return 'href="' + target + '"'

    page = re.sub(r'href="([^\"]+)"', replace_link, page)
    output = ROOT / "yangtze-portfolio-preview.html"
    output.write_text(page)
    print(output.name + ": " + str(round(output.stat().st_size / 1_000_000, 2)) + " MB")


if __name__ == "__main__":
    build()
