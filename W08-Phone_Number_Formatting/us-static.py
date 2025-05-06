def format_phone_number(pn: list[int]) -> str:
    return f"({pn[0]}{pn[1]}{pn[2]}) {pn[3]}{pn[4]}{pn[5]}-{pn[6]}{pn[7]}{pn[8]}{pn[9]}"

output = format_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print( "success" if "(123) 456-7890" == output else "failure")
output = format_phone_number([5, 1, 9, 5, 5, 5, 4, 4, 6, 8])
print( "success" if "(519) 555-4468" == output else "failure")
output = format_phone_number([3, 4, 5, 5, 0, 1, 2, 5, 2, 7])
print( "success" if "(345) 501-2527" == output else "failure")