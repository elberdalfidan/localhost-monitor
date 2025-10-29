"""Main application entry point for Localhost Monitor."""

import rumps
import threading
from typing import Dict, List

import src.config as config
import src.port_scanner as port_scanner
import src.process_monitor as process_monitor
import src.ui_helpers as ui_helpers
import src.quick_actions as quick_actions
import src.updater as updater


class LocalhostMonitorApp(rumps.App):
    """Main menubar application class."""

    def __init__(self):
        super(LocalhostMonitorApp, self).__init__(
            name=config.APP_NAME,
            icon=config.APP_ICON,
            template=True,  # Template mode: icon adapts to light/dark menu bar
            quit_button=None  # We'll add our own quit button
        )

        # Store current processes
        self.processes: Dict[int, Dict] = {}  # port -> process info
        self.is_scanning = False

        # Initialize update checker
        self.updater = updater.UpdateChecker(self)

        # Build initial menu
        self.menu = [
            rumps.MenuItem("Refresh", callback=self.refresh_processes),
            rumps.separator,
            rumps.MenuItem("Quit", callback=self.quit_app)
        ]

        # Start initial scan
        self.refresh_processes(None)

        # Check for updates on startup (delayed, silent)
        if config.ENABLE_AUTO_UPDATE_CHECK:
            rumps.Timer(
                self._check_updates_startup,
                config.UPDATE_CHECK_ON_STARTUP_DELAY
            ).start()

    def refresh_processes(self, sender):
        """Refresh the list of processes and update menu."""
        if self.is_scanning:
            return

        self.is_scanning = True

        try:
            # Scan for ports
            ports_info = port_scanner.scan_ports(
                config.PORT_RANGE_START,
                config.PORT_RANGE_END
            )

            # Update process cache
            self.processes.clear()
            for port_info in ports_info:
                proc_info = process_monitor.get_process_info(port_info['pid'])
                if proc_info:
                    self.processes[port_info['port']] = {**port_info, **proc_info}

            # Update title (icon shows separately, just show count)
            self.title = f"{len(self.processes)}" if self.processes else ""

            # Rebuild menu with new section-based structure
            self.menu.clear()
            self.menu = self.build_menu()

        except Exception as e:
            print(f"Error refreshing processes: {e}")
            self.title = "!"  # Error indicator
            self.menu = self.build_error_menu(str(e))
        finally:
            self.is_scanning = False

    def build_menu(self) -> List:
        """
        Build the complete menu with section-based structure.

        Returns:
            List of menu items
        """
        menu = []

        # ═══ ACTIVE PROCESSES Section ═══
        menu.extend(self.build_processes_section())

        # ═══ QUICK ACTIONS Section ═══
        menu.extend(self.build_quick_actions_section())

        # ═══ ABOUT Section ═══
        menu.extend(self.build_about_section())

        # Separator and Quit
        menu.append(rumps.separator)
        menu.append(rumps.MenuItem("Quit", callback=self.quit_app))

        return menu

    def build_processes_section(self) -> List:
        """Build the ACTIVE PROCESSES section."""
        section = []

        # Section header
        header = ui_helpers.create_section_header("ACTIVE PROCESSES")
        if header:
            section.append(header)

        # Process list
        if not self.processes:
            section.append(rumps.MenuItem("No active processes", callback=None))
        else:
            for port in sorted(self.processes.keys()):
                proc_info = self.processes[port]
                proc_menu = self.create_process_menu(port, proc_info)
                section.append(proc_menu)

        return section

    def build_quick_actions_section(self) -> List:
        """Build the QUICK ACTIONS section."""
        section = []

        # Section separator and header
        section.append(rumps.separator)
        header = ui_helpers.create_section_header("QUICK ACTIONS")
        if header:
            section.append(header)

        # Refresh
        section.append(rumps.MenuItem("Refresh", callback=self.refresh_processes))

        # Kill All (if enabled)
        if config.ENABLE_KILL_ALL:
            kill_all = rumps.MenuItem("Kill All Ports", callback=self.kill_all_callback)
            section.append(kill_all)

        # Favorites (coming soon)
        if config.ENABLE_FAVORITES:
            # Active when implemented
            section.append(rumps.MenuItem("Favorites", callback=self.favorites_callback))
        else:
            # Placeholder
            section.append(ui_helpers.create_disabled_feature_item("Favorites", "0.2.1"))

        return section

    def build_about_section(self) -> List:
        """Build the ABOUT section."""
        section = []

        # Section separator and header
        section.append(rumps.separator)
        header = ui_helpers.create_section_header("ABOUT")
        if header:
            section.append(header)

        # About dialog
        section.append(rumps.MenuItem("About", callback=lambda _: ui_helpers.show_about_dialog()))

        # Website
        section.append(rumps.MenuItem("Website", callback=lambda _: ui_helpers.open_website()))

        # Update checker
        section.append(rumps.separator)
        section.append(rumps.MenuItem("Check for Updates", callback=self.check_for_updates_callback))

        # Settings (coming soon)
        if config.ENABLE_SETTINGS_GUI:
            section.append(rumps.MenuItem("Settings", callback=self.settings_callback))
        else:
            section.append(ui_helpers.create_disabled_feature_item("Settings", "0.2.2"))

        return section

    def build_error_menu(self, error_msg: str) -> List:
        """Build error menu when something goes wrong."""
        return [
            rumps.MenuItem(f"Error: {error_msg}", callback=None),
            rumps.separator,
            rumps.MenuItem("Refresh", callback=self.refresh_processes),
            rumps.separator,
            rumps.MenuItem("Quit", callback=self.quit_app)
        ]

    def create_process_menu(self, port: int, proc_info: Dict) -> rumps.MenuItem:
        """
        Create a menu item for a process with submenu.

        Args:
            port: Port number
            proc_info: Process information dictionary

        Returns:
            rumps.MenuItem with submenu
        """
        # Main item: Port and process name (with favorite support)
        is_favorite = False  # TODO: Check favorites in Phase 2.1
        title = ui_helpers.format_process_title(port, proc_info['name'], is_favorite)
        port_item = rumps.MenuItem(title)

        # Create submenu items using helper
        submenu_items = []

        if config.SHOW_PID:
            submenu_items.append(
                ui_helpers.create_process_stat_item("PID", str(proc_info['pid']))
            )

        if config.SHOW_RAM:
            submenu_items.append(
                ui_helpers.create_process_stat_item("RAM", f"{proc_info['memory_mb']} MB")
            )

        if config.SHOW_CPU:
            submenu_items.append(
                ui_helpers.create_process_stat_item("CPU", f"{proc_info['cpu_percent']}%")
            )

        if config.SHOW_UPTIME:
            submenu_items.append(
                rumps.MenuItem(f"Uptime: {proc_info['uptime_formatted']}", callback=None)
            )

        # Add separator and kill button
        submenu_items.append(rumps.separator)
        kill_button = rumps.MenuItem(
            "Kill Process",
            callback=lambda sender: self.kill_process_callback(port, proc_info['pid'])
        )
        submenu_items.append(kill_button)

        # Assign submenu
        port_item.update(submenu_items)

        return port_item

    def kill_process_callback(self, port: int, pid: int):
        """
        Callback for kill process button.

        Args:
            port: Port number
            pid: Process ID to kill
        """
        try:
            # Confirmation dialog
            response = rumps.alert(
                title="Kill Process",
                message=f"Are you sure you want to kill process on port {port} (PID: {pid})?",
                ok="Kill",
                cancel="Cancel"
            )

            if response == 1:  # OK clicked
                success = process_monitor.kill_process(pid)

                if success:
                    rumps.notification(
                        title="Process Killed",
                        subtitle=f"Port {port}",
                        message=f"Process {pid} has been terminated"
                    )

                    # Refresh menu after short delay
                    threading.Timer(0.5, lambda: self.refresh_processes(None)).start()
                else:
                    rumps.alert(
                        title="Error",
                        message=f"Failed to kill process {pid}. Try again or use force kill.",
                        ok="OK"
                    )

        except Exception as e:
            rumps.alert(
                title="Error",
                message=f"Error killing process: {str(e)}",
                ok="OK"
            )

    @rumps.timer(config.REFRESH_INTERVAL)
    def auto_refresh(self, sender):
        """Auto-refresh timer callback."""
        self.refresh_processes(None)

    def kill_all_callback(self, sender):
        """Callback for Kill All Ports action."""
        quick_actions.execute_kill_all(self.processes)

        # Refresh menu after short delay
        threading.Timer(1.0, lambda: self.refresh_processes(None)).start()

    def favorites_callback(self, sender):
        """Callback for Favorites action (placeholder)."""
        ui_helpers.show_info_dialog(
            title="Feature Coming Soon",
            message="Favorites will be available in v0.2.1"
        )

    def settings_callback(self, sender):
        """Callback for Settings action (placeholder)."""
        ui_helpers.show_info_dialog(
            title="Feature Coming Soon",
            message="Settings GUI will be available in v0.2.2"
        )

    def _check_updates_startup(self, sender):
        """Check for updates on startup (runs once, silent mode)."""
        self.updater.check_for_updates(silent=True)

    def check_for_updates_callback(self, sender):
        """Manually check for updates (shows result)."""
        self.updater.check_for_updates(silent=False)

    def quit_app(self, sender):
        """Quit the application."""
        rumps.quit_application()


def main():
    """Main entry point."""
    app = LocalhostMonitorApp()
    app.run()


if __name__ == "__main__":
    main()
