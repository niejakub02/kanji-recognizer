# Run after installing Noto Sans JP font

import shutil
import matplotlib
import matplotlib.font_manager as fm
from consts import matplotlib_title_font


if __name__ == "__main__":
    shutil.rmtree(matplotlib.get_cachedir())
    is_installed = False

    for f in fm.fontManager.ttflist:
        if f.name == matplotlib_title_font["fontname"]:
            is_installed = True

    print(
        matplotlib_title_font["fontname"],
        "font is installed" if is_installed else "font is NOT installed",
    )
