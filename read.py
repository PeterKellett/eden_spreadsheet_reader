from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1BbkF3n8NKAacdAle7atDHNo-YfnQI8PvDsv0BvuE0S8"

service = build("sheets", "v4", credentials=creds)
print("Reading...")
# Call the Sheets API
sheet = service.spreadsheets()
result = (
    sheet.values()
    .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Input")
    .execute()
)
values = result.get("values", [])
# print("values = ", values)
output = []
new_row = []
numerator = ' '
denominator = ' '
print("Formatting...")
for item in values:
    if item:
        # print("item = ", item)
        split_string = item[0].split(' ')
        if split_string[0][-1] == '.':
            if new_row:
                new_row.append(numerator)
                new_row.append(denominator)
                output.append(new_row)
                new_row = []
                # print(f"split_string = {item[0]}")
            new_row.append(item[0])
        elif 'Minutes' in item[0]:
            # print("YES")
            numerator = ' '
            denominator = ' '
            # new_row.append('')
            new_row.append(item[0])
        elif '/' in item[0]:
            new_row.append(item[0])
            # new_row.append('')
            split_string = item[0].split('/')
            # print("split_string = ", split_string)
            numerator = split_string[0]
            split_string_further = split_string[1].split(' ')
            denominator = split_string_further[1]
        else: 
            new_row.append(item[0])
output.append(new_row)
# print("output = ", output)
print("Writing...")
result = (
    sheet.values().update(
        spreadsheetId=SAMPLE_SPREADSHEET_ID,
        range="Format!A1",
        valueInputOption="USER_ENTERED",
        body={"values": output},
    )
    .execute()
)
print("DONE!!")
