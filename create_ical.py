import datetime

def create_ical(rows_ical):

    ical_file = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//OpenAI//Assistant//EN
CALSCALE:GREGORIAN
METHOD:PUBLISH

"""

    i = 0
    for row in rows_ical:
        row[1] = row[1].replace(" ", "")
        if row[1] != "X":
            ical_file += """BEGIN:VEVENT
UID:event"""+str(i)+"""@example.com
DTSTART:"""+row[1]+"""
DTEND:"""+row[1]+"""
SUMMARY:"""+row[0]+"""
DESCRIPTION:"""+row[2]+"""
END:VEVENT

"""
        i += 1

    ical_file += """END:VCALENDAR

"""
    with open("this.ics", 'w') as file:
        file.write(ical_file)
