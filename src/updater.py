"""Simple update checker for Localhost Monitor."""

import urllib.request
import json
import webbrowser
import rumps
import src.config as config


class UpdateChecker:
    """Check for app updates via GitHub API."""

    REPO_URL = "https://api.github.com/repos/elberdalfidan/localhost-monitor/releases/latest"
    RELEASES_PAGE = "https://github.com/elberdalfidan/localhost-monitor/releases"

    def __init__(self, app):
        """
        Initialize update checker.

        Args:
            app: Main application instance
        """
        self.app = app
        self.current_version = config.APP_VERSION

    def check_for_updates(self, silent=True):
        """
        Check if newer version is available.

        Args:
            silent: If True, only notify if update available
                   If False, always show result
        """
        try:
            update_info = self._fetch_latest_release()

            if update_info["available"]:
                self._show_update_notification(update_info)
            elif not silent:
                rumps.notification(
                    title="No Updates Available",
                    subtitle=f"You have the latest version ({self.current_version})",
                    message="Localhost Monitor is up to date!"
                )
        except Exception as e:
            if not silent:
                rumps.notification(
                    title="Update Check Failed",
                    subtitle="Could not connect to update server",
                    message=str(e)
                )

    def _fetch_latest_release(self):
        """
        Fetch latest release info from GitHub API.

        Returns:
            Dict with update information
        """
        request = urllib.request.Request(
            self.REPO_URL,
            headers={"Accept": "application/vnd.github.v3+json"}
        )

        with urllib.request.urlopen(request, timeout=10) as response:
            data = json.loads(response.read())

        latest_version = data["tag_name"].lstrip("v")

        # Compare versions
        is_newer = self._is_version_newer(latest_version, self.current_version)

        return {
            "available": is_newer,
            "version": latest_version,
            "url": data["html_url"],
            "download_url": self._get_dmg_url(data),
            "release_notes": data["body"][:200] if data.get("body") else ""
        }

    def _is_version_newer(self, latest, current):
        """
        Compare version strings (e.g., '0.3.0' > '0.2.0').

        Args:
            latest: Latest version string
            current: Current version string

        Returns:
            True if latest is newer than current
        """
        try:
            latest_parts = [int(x) for x in latest.split(".")]
            current_parts = [int(x) for x in current.split(".")]

            return latest_parts > current_parts
        except (ValueError, AttributeError):
            return False

    def _get_dmg_url(self, release_data):
        """
        Extract DMG download URL from release assets.

        Args:
            release_data: GitHub release data

        Returns:
            DMG download URL or None
        """
        for asset in release_data.get("assets", []):
            if asset["name"].endswith(".dmg"):
                return asset["browser_download_url"]
        return None

    def _show_update_notification(self, update_info):
        """
        Show notification about available update.

        Args:
            update_info: Update information dictionary
        """
        rumps.notification(
            title=f"Update Available: v{update_info['version']}",
            subtitle=f"Current version: {self.current_version}",
            message="Click 'Check for Updates' in the menu to download."
        )

    def open_releases_page(self):
        """Open GitHub releases page in default browser."""
        try:
            webbrowser.open(self.RELEASES_PAGE)
        except Exception as e:
            rumps.alert(
                title="Error",
                message=f"Could not open releases page: {str(e)}",
                ok="OK"
            )
