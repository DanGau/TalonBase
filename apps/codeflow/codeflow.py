from talon import Module
from typing import Union

mod = Module()

mod.apps.codeflow = """
os: windows
and app.name: CodeFlow
"""

@mod.action_class
class Actions:
    # Navigation
    def codeflow_next_change():
        """Navigates to the next changed block of code"""
    def codeflow_last_change():
        """Navigates to the last changed block of code"""
    def codeflow_next_file():
        """Navigates to the next file"""
    def codeflow_last_file():
        """Navigates to the last file"""
    def codeflow_next_comment():
        """Navigates to the next active comment"""
    def codeflow_last_comment():
        """Navigates to the last active comment"""
    # def codeflow_go_to_find():
    #    """Navigates to the file search box"""

    # Iterations
    # def codeflow_iteration_num(num: Union[int, str]):
    #    """Goes to the given iteration number"""
    # def codeflow_iteration_diff(num1: Union[int, str], num2: Union[int, str]):
    #    """Diffs two iterations"""

    # Review
    def codeflow_show_both():
        """Shows left and right changes"""
    def codeflow_show_left():
        """Shows only left (removed) changes"""
    def codeflow_show_right():
        """Shows only right (removed) changes"""

    # Comments
    def codeflow_comment_add():
        """Adds a new comment at the cursor"""
    def codeflow_comment_publish():
        """Publishes the current open comment"""
    # def user.codeflow_comment_resolve():
    #    """Marks the active comment resolved"""
    # def codeflow_comment_active():
    #    """Marks the active comment active"""
    # def codeflow_comment_pending():
    #    """Marks the active comment pending"""
    # def codeflow_comment_closed():
    #    """Marks the active comment closed"""
    # def codeflow_comment_wontfix():
    #    """Marks the active comment as won't fix"""

    # Status
    def codeflow_status_approve():
        """Marks your reviewer status as approved"""
    def codeflow_status_suggestions():
        """Marks your reviewer status as approved with suggestions"""
    def codeflow_status_waiting():
        """Marks your reviewer status as waiting"""
    def codeflow_status_reset():
        """Resets your reviewer status"""
    def codeflow_status_reject():
        """Marks your reviewer status as reject"""