import argparse
from argparse import RawTextHelpFormatter


def hello(args):
    name = args.name
    greeting = 'Hello, {}'.format(name)

    print(greeting)


class Arg:
    def __init__(self, flags=None, help=None, action=None, default=None, nargs=None, type=None, choices=None):
        self.flags = flags
        self.help = help
        self.action = action
        self.default = default
        self.nargs = nargs
        self.type = type
        self.choices = choices


class CLIFactory:
    args = {
        'name': Arg(
            ("--name",),
            default='World',
            help='Name for greeting'
        ),
    }

    subparsers = (
        {
            'func': hello,
            'help': 'Generate a nice greeting',
            'args': ('name',)
        },
    )

    subparsers_dict = {sp['func'].__name__: sp for sp in subparsers}

    @classmethod
    def get_parser(cls):
        parser = argparse.ArgumentParser()

        subparsers = parser.add_subparsers(help='sub-command help', dest='subparser')
        subparsers.required = True

        subparser_list = cls.subparsers_dict.keys()

        for sub in subparser_list:
            sub = cls.subparsers_dict[sub]

            sp = subparsers.add_parser(sub['func'].__name__, help=sub['help'])
            sp.formatter_class = RawTextHelpFormatter

            for arg in sub['args']:
                arg = cls.args[arg]

                kwargs = {
                    f: v for f, v in vars(arg).items() if f != 'flags' and v
                }

                sp.add_argument(*arg.flags, **kwargs)

            sp.set_defaults(func=sub['func'])

        return parser
