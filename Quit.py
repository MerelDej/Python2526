class QuitToMenu(Exception):
    """Raised when user wants to quit current command"""
    pass

def safe_input(q):
    value = input(q).strip()
    if value.lower() == "q":
        print("\nCancelled. Returning to menu...\n")
        raise QuitToMenu
    return value