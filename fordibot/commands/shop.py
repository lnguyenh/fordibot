from datetime import datetime

import imgkit
from fordibot.apis.fortniteio.client import FORTNITE_IO_API_CLIENT


SMALL_WIDTH_FORCING_MARGIN_REMOVAL = 500


async def generate_shop():
    items = fetch_shop()
    pictures = [item["displayAssets"][0]["full_background"] for item in items]
    as_html = generate_html(pictures)
    as_png = convert_to_png(as_html)
    filename = f"shop-{datetime.now()}.png"
    return as_png, filename


def chunks(my_list, n):
    for i in range(0, len(my_list), n):
        yield my_list[i : i + n]


def generate_html(pictures):
    lines = ["<html><body style = 'margin:0px;padding:0px;' ><table>"]
    for chunk in chunks(pictures, 8):
        lines.append("<tr>")
        for image in chunk:
            lines.append(f"<td><img src='{image}' width='150'></td>")
        lines.append("</tr>")
    lines.append("</table></body></html>")
    return "\n".join(lines)


def convert_to_png(html_content):
    options = {"format": "png", "width": SMALL_WIDTH_FORCING_MARGIN_REMOVAL}
    return imgkit.from_string(html_content, False, options=options)


def fetch_shop():
    return FORTNITE_IO_API_CLIENT.get_shop().json()["shop"]


if __name__ == "__main__":
    generate_shop()
