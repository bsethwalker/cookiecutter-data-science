from .bin.cli import CLIFactory


def main():
	parser = CLIFactory.get_parser()
	args = parser.parse_args()
	args.func(args)
