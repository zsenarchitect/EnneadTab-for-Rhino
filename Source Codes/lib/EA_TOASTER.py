import subprocess


def toast(message, title, app_name, icon, click, actions):
    """Send toast notificaton.
    Args:
        click (str): click action (see `--activation-arg` cli option)
        actions (dict[str:str]):
            list of actions (see `--action` and `--action-arg` cli options)
    """
    def get_toaster():
        """Return full file path of the toast binary utility."""
        return r"L:\4b_Applied Computing\03_Rhino\12_EnneadTab for Rhino\Source Codes\lib\ennead.exe"


    # set defaults
    if not icon:
        icon = r"L:\4b_Applied Computing\03_Rhino\12_EnneadTab for Rhino\Source Codes\lib\toaster_icon.png"
    if not actions:
        actions = {}

    # build the toast
    toast_args = r'"{}"'.format(get_toaster())
    toast_args += r' --app-id "{}"'.format(app_name)
    toast_args += r' --title "{}"'.format(title)
    toast_args += r' --message "{}"'.format(message)
    toast_args += r' --icon "{}"'.format(icon)
    toast_args += r' --audio "default"'
    # toast_args += r' --duration "long"'
    if click:
        toast_args += r' --activation-arg "{}"'.format(click)
    for action, args in actions.items():
        toast_args += r' --action "{}" --action-arg "{}"'.format(action, args)

    # send the toast now
    subprocess.Popen(toast_args, shell = True)

if __name__ == "__main__":
    toast("123")
