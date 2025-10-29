"""UI helper functions for menubar app."""

import rumps
import webbrowser
from typing import Optional

import src.config as config


def create_section_header(title: str) -> rumps.MenuItem:
    """
    Create a disabled menu item as a section header.

    Args:
        title: Section title text

    Returns:
        Disabled menu item formatted as header
    """
    if not config.SHOW_SECTIONS:
        return None

    # Choose style based on config
    if config.SECTION_STYLE == "equals":
        formatted_title = f"═══ {title.upper()} ═══"
    elif config.SECTION_STYLE == "dashes":
        formatted_title = f"─── {title.upper()} ───"
    else:
        formatted_title = title.upper()

    # Create disabled menu item (acts as visual separator)
    header = rumps.MenuItem(formatted_title, callback=None)
    return header


def show_about_dialog():
    """
    Show the About dialog with app information.

    Displays:
    - App name and version
    - Author and license
    - Description
    - Visit Website button
    """
    message = (
        f"Version: {config.APP_VERSION}\n"
        f"Author: {config.APP_AUTHOR}\n"
        f"License: {config.APP_LICENSE}\n\n"
        f"{config.APP_DESCRIPTION}\n"
    )

    response = rumps.alert(
        title=f"{config.APP_NAME}",
        message=message,
        ok="Visit Website",
        cancel="Close"
    )

    # If user clicked "Visit Website" (response == 1)
    if response == 1:
        open_website()


def open_website():
    """Open the app website in default browser."""
    try:
        webbrowser.open(config.WEBSITE_URL)
    except Exception as e:
        rumps.alert(
            title="Error",
            message=f"Could not open website: {str(e)}",
            ok="OK"
        )


def show_confirmation_dialog(title: str, message: str, ok_text: str = "OK", cancel_text: str = "Cancel") -> bool:
    """
    Show a confirmation dialog.

    Args:
        title: Dialog title
        message: Dialog message
        ok_text: OK button text
        cancel_text: Cancel button text

    Returns:
        True if user clicked OK, False if cancelled
    """
    response = rumps.alert(
        title=title,
        message=message,
        ok=ok_text,
        cancel=cancel_text
    )

    return response == 1


def show_info_dialog(title: str, message: str):
    """
    Show an informational dialog.

    Args:
        title: Dialog title
        message: Dialog message
    """
    rumps.alert(
        title=title,
        message=message,
        ok="OK"
    )


def format_process_title(port: int, name: str, is_favorite: bool = False) -> str:
    """
    Format process menu item title.

    Args:
        port: Port number
        name: Process name
        is_favorite: Whether this is a favorite process

    Returns:
        Formatted title string
    """
    status = "[FAVORITE]" if is_favorite else "[ACTIVE]"
    return f"{status} :{port} → {name}"


def create_disabled_feature_item(title: str, coming_version: str) -> rumps.MenuItem:
    """
    Create a disabled menu item for features coming soon.

    Args:
        title: Feature name
        coming_version: Version when feature will be available

    Returns:
        Disabled menu item with "(coming soon)" suffix
    """
    item_title = f"{title} (v{coming_version})"
    item = rumps.MenuItem(item_title, callback=None)
    return item


def create_process_stat_item(label: str, value: str) -> rumps.MenuItem:
    """
    Create a non-interactive menu item displaying process stats.

    Args:
        label: Stat label (e.g., "RAM")
        value: Stat value (e.g., "245 MB")

    Returns:
        Disabled menu item
    """
    return rumps.MenuItem(f"{label}: {value}", callback=None)
