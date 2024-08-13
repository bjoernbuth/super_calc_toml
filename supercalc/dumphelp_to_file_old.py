import click
import supercalc.click_options_abbrevs as click_abbrevs
import supercalc.constants as constants
import dataclasses

import supercalc.main as main
import re
import pyperclip


@dataclasses.dataclass
class HelpConfig:
    """Dataclass for the help configuration.

    - dotted_name: str = ""
    - dotted_section: str = "1"
    - is_root: bool = False
    - level: int = 1
    - number_sections: bool = False
    - parent: str | None = None
    """

    dotted_name: str = ""
    dotted_section: str = "1"
    is_root: bool = False
    level: int = 1
    number_sections: bool = False
    parent: str | None = None


@click.command()
@click_abbrevs.copy_to_clipboard_option
@click_abbrevs.help_shorter_option
@click_abbrevs.print_result_option
@click.option(
    "--number_sections/--no_number_sections",
    "--ns/--nons",
    is_flag=True,
    default=False,
    show_default=True,
    help="Print result to console.",
)
def dumphelp_to_file(
    copy_to_clipboard: bool = True,
    print_result: bool = True,
    number_sections: bool = False,
):
    """Dump the help to ../docs/dump_help.md."""
    target_file = constants.PROJECT_ROOT / "doc" / "dump_help.md"

    help_config = HelpConfig(
        dotted_name="",
        dotted_section="1",
        is_root=True,
        level=1,
        number_sections=number_sections,
        parent=None,
    )

    lines = recursive_help(cmd=main.suca, help_config=help_config)

    # Remove the lines matching the pattern "Usage:" other stuff [OPTIONS] other stuff
    pattern = r".*Usage.*\n*"
    # remove all lines matching the pattern

    modified_lines = []
    for line in lines:
        line = re.sub(pattern, "", line)
        modified_lines.append(line)

    lines = modified_lines

    res_text = "\n".join(lines)

    pattern_2 = r"```\n  "  # fix indent at the beginning of the code block
    res_text = re.sub(pattern_2, "```\n", res_text)

    if print_result:
        print(res_text)
        # print("hi")

    with open(target_file, "w") as f:
        f.write(res_text)
        print("Dumped help to", target_file)

    # re.sub(pattern, "", res_text)

    if copy_to_clipboard:
        pyperclip.copy(res_text)
        print("Result copied to clipboard.")


def recursive_help(
    *,
    cmd,
    help_config: HelpConfig,
) -> list[str]:
    """For a given command or group, print the help for the command and all subcommands
    recursively.

    Args (keyword only):
    - cmd:  click.core.Command or click.core.Group
            he command or group for which to print the help.
    - parent (click.core.Context: The parent command context.
    - dotted_name (str): The dotted name of the command.
    - level (int): The level of the command in the command hierarchy.
    - is_root (bool=False): Marker for the root node.
    - dotted_section (str): The dotted section , e.g. 1.2.3 cli_command_name
    - number_sections (bool=default False): If True, number the sections.
    """
    short_help = cmd.get_short_help_str()
    lines = []

    section_string = ""

    if help_config.number_sections:
        section_string = f"{help_config.dotted_section} "

    if help_config.is_root:
        help_config.dotted_name = cmd.name
        lines.append(f"# {section_string} {help_config.dotted_name} \n")
    elif isinstance(cmd, click.core.Group):
        lines.append(
            f"{help_config.level*'#'} {section_string} {help_config.dotted_name} - group\n"
        )
    else:  # sub is a command
        lines.append(
            f"{help_config.level*'#'} {section_string} {help_config.dotted_name} - command\n"
        )

    ctx = click.core.Context(cmd, info_name=cmd.name, parent=help_config.parent)
    lines.append("```\n" + cmd.get_help(ctx) + "\n```" + "\n")

    commands = getattr(cmd, "commands", {})
    # print("1", type(commands), commands)
    for cmd_number, sub in enumerate(commands.values(), start=1):
        # check if the sub is a group
        # print_sep()

        new_help_config = HelpConfig(
            dotted_name=help_config.dotted_name + "." + sub.name,
            dotted_section=help_config.dotted_section + f".{cmd_number}",
            level=help_config.level + 1,
            is_root=False,
            number_sections=help_config.number_sections,
            parent=ctx,
        )

        new_lines = recursive_help(cmd=sub, help_config=new_help_config)
        lines.extend(new_lines)

    return lines


if __name__ == "__main__":
    dumphelp_to_file()