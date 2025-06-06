def sort(width, height, length, mass):
    """  Sort packages based on width, height, length, and mass."""
    volume = width * height * length
    package = []
    if volume >= 1000000:
        package.append("BULKY")
    if width >= 150:
        package.append("BULKY")
    if height >= 150:
        package.append("BULKY")
    if length >= 150:
        package.append("BULKY")
    if mass >= 20:
        package.append("HEAVY")

    if "BULKY" in package:
        if "HEAVY" in package:
            stack = "REJECTED"
        else:
            stack = "SPECIAL"
    elif "HEAVY" in package:
        stack = "SPECIAL"
    else:
        stack = "STANDARD"
    
    return stack