"""
Rich-based terminal display helpers shared across both pipeline modes.
"""

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box

console = Console()


def header(title: str, subtitle: str = "") -> None:
    text = Text(title, style="bold white")
    if subtitle:
        text.append(f"\n{subtitle}", style="dim")
    console.print(Panel(text, box=box.DOUBLE_EDGE, border_style="cyan"))


def agent_log(agent_name: str, message: str, style: str = "white") -> None:
    tag = Text(f"[{agent_name}]", style=f"bold {_agent_color(agent_name)}")
    console.print(tag, Text(message, style=style))


def warning(message: str) -> None:
    console.print(f"  [bold yellow]⚠[/bold yellow]  {message}")


def success(message: str) -> None:
    console.print(f"  [bold green]✓[/bold green]  {message}")


def error(message: str) -> None:
    console.print(f"  [bold red]✗[/bold red]  {message}")


def info(message: str) -> None:
    console.print(f"  [dim]→[/dim]  {message}")


def divider(label: str = "") -> None:
    if label:
        console.rule(f"[dim]{label}[/dim]")
    else:
        console.rule()


def collision_box(message: str) -> None:
    console.print(
        Panel(
            Text(message, style="bold red"),
            title="[bold red]COLLISION DETECTED[/bold red]",
            border_style="red",
            box=box.HEAVY,
        )
    )


def resolved_box(message: str) -> None:
    console.print(
        Panel(
            Text(message, style="bold green"),
            title="[bold green]CONFLICT AVOIDED[/bold green]",
            border_style="green",
            box=box.HEAVY,
        )
    )


def _agent_color(agent_name: str) -> str:
    colors = {
        "Planner": "magenta",
        "Coder": "blue",
        "Reviewer": "yellow",
    }
    return colors.get(agent_name, "white")
