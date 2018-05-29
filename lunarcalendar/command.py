# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
import os
import sys
from argparse import ArgumentParser, RawDescriptionHelpFormatter

from lunarcalendar.color import red, blue
from lunarcalendar._compact import unicode_type
from lunarcalendar import __version__
from lunarcalendar.festival import zh_festivals


DESCRIPTION = """Search festivals by chinese-name. """

EPILOG = """
eg: lunar-find 中秋 [2018]
eg: lunar-find -a [2018]

Recommended time range: 1900 - 2100, which may be enough.
If not, you must extend it before expect it working well.

For documentation, source code and other information, please visit:
<https://github.com/wolfhong/LunarCalendar>_.

You're welcome to contribute to this project, or offer some suggestions
about festival, come on and open an issue please:
<https://github.com/wolfhong/LunarCalendar/issues>_.
"""


def create_parser():
    parser = ArgumentParser(
        formatter_class=RawDescriptionHelpFormatter,
        description=DESCRIPTION,
        epilog=EPILOG,
        add_help=False)

    fest = parser.add_argument_group("Festival")
    fest.add_argument(
        dest="name",
        action="store",
        default="",
        nargs="?",
        help="""Name of the festival.
If Name is all, print all included festivals by date asc and then exit.
""")
    fest.add_argument(
        dest="year",
        action="store",
        default=None,
        nargs="?",
        type=int,
        help="Year (default to this year)")

    info = parser.add_argument_group("Information")
    info.add_argument(
        '-h',
        '--help',
        action='store_true',
        default=False,
        help="Prints this help and exits")
    info.add_argument(
        '--version',
        action='store_true',
        default=False,
        help="Prints the version and exits")
    return parser


def format_output(fest, year, search_name=None, name_width=None):
    first_name = fest.get_lang('zh')
    if name_width:
        first_name = "  " * (name_width-len(first_name)) + first_name

    if search_name and search_name != first_name:
        format_name = "{}({})".format(blue(first_name), search_name)
    else:
        format_name = blue(first_name)

    output = "{} on {}: {}".format(format_name, year, red(fest(year)), )
    sys.stdout.write(output + os.linesep)


def main(*args):
    parser = create_parser()
    args = parser.parse_args(args if args else None)
    # print(args)

    year = args.year if args.year else datetime.datetime.now().year
    name = args.name if args.name else ""
    if not isinstance(name, unicode_type):
        name = name.decode(sys.stdin.encoding)

    if args.help:
        parser.print_help()
    elif args.version:
        sys.stdout.write(__version__ + os.linesep)
    elif not name:  # syntax error
        parser.print_help()
        return 1
    elif name == 'all':
        max_width = max([len(f.get_lang('zh')) for f in zh_festivals])
        [format_output(f, year, name_width=max_width) for f in sorted(zh_festivals, key=lambda _f: _f(year))]
    else:
        result_list = []
        for fest in zh_festivals:
            for zhname in fest.get_lang_list('zh'):
                if zhname == name:
                    format_output(fest, year, search_name=name)
                    return 0  # 100% matched, print and exit
                elif zhname.find(name) >= 0 and (len(name) * 1.0 / len(zhname) > 0.5):
                    result_list.append((fest, name))  # not 100% matched, store result
                    break

        # not found, but matched
        for fest, search_name in result_list:
            format_output(fest, year, search_name=search_name)

    return 0


def find():
    result = main()
    exit(result)


if __name__ == "__main__":
    main(*sys.argv[1:])
