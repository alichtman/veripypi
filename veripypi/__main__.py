import click
from colorama import Fore, Style
from constants import ProjInfo


def print_usage():
	print("USAGE: $ veripypi [PKG_NAME] [GITHUB_AUTHOR_PKG]")
	print("EX:    $ veripypi shallow-backup alichtman/shallow-backup")


def print_version(splash=False):
	"""
	Format version differently for CLI and splash screen.
	"""
	version = "v{} by {} (@{})".format(ProjInfo.VERSION,
	                                   ProjInfo.AUTHOR_FULL_NAME,
	                                   ProjInfo.AUTHOR_GITHUB)
	if splash:
		print(Fore.RED + Style.BRIGHT + "\t{}\n".format(version) + Style.RESET_ALL)
	else:
		print(version)


@click.command(context_settings=dict(help_option_names=['-h', '-help', '--help']))
@click.argument('pypi', help='Pypi package name')
@click.argument('github', help='Github project in [author/repo] format.')
@click.option('--version', '-v', is_flag=True, default=False, help='Display version and author info.')
def main(pypi, github, version):
	# Input validation
	if version:
		print_version()
	if not pypi or not github:
		print_usage()
		return

	print_version(splash=True)

	# TODO: Contain this so that untrusted code can be run more safely?
	# 		Maybe do this in a series of checks. First compare the setup.py files,
	# 		then if those match, run the installer and go from there?
	# TODO: Create sdist from latest release of a GitHub repo of the package to be verified.
	# TODO: Install PyPi version of the package
	# TODO: Compare the two installations
	# TODO: Clean up
	# TODO: Display success/failure.
	pass


if __name__ == '__main__':
	main()
