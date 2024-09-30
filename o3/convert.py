# importing modules
import requests
import time

# API endpoint to merge pdfs
url = "https://api.pdf.co/v1/pdf/merge"

# API endpoint to convert pdf to json
url_json = "https://api.pdf.co/v1/pdf/convert/to/json2"

# defining parameter
api_key = "pravinb19@gmail.com_sTE9lIp4gtahYNmJ8FbFk09rWoz8HRrPgxPseXYxEVKExGNDF69l5vmHlkxWWwwj"

# files to be merged
rbfs_guide = "https://drive.google.com/file/d/1M26h_fvE0szFWSF6v85CitQ9f2LDGk9E/view?usp=drive_link"
troubleshooting = "https://drive.google.com/file/d/1XeqP-eL1_Hmdy_t3SeTxpm2lsY6PebRO/view?usp=drive_link"
reference = "https://drive.google.com/file/d/1Mw7wfESen6Mc2QyI_nZAkGSpaMsEcgi7/view?usp=drive_link"
api_reference = "https://drive.google.com/file/d/1J7DN9CDTKYV0Cg137E_xpHwu0wF_GMP2/view?usp=drive_link"
file_url = ""


# combining file urls, separated by comma
files = rbfs_guide + ',' + troubleshooting + ',' + reference + ',' + api_reference

def pdf_to_json(file_url):
    tries = 3

    # try atleast three time if the request gets failed
    while (tries >= 0):
        # post request to the API endpoint to merge to pdf files
        response = requests.post(url_json,
        headers={
        "x-api-key": api_key
        },
        data={
        "url": file_url
        }
    )

    # checking if the request is successful or not
    if response.status_code == 200:
        print(response)
        response_json = response.json()
        print(response_json)
    else:
        tries = tries -1

    # sleep for some time
    time.sleep(0.5)
    print("request failed, trying again")
    print("request failed, returning")

# function to merge to pdf files
def merge_files_output_JSON():
    tries =3

    # try at least three times if the request gets failed
    while (tries >= 0):
        print(files)
    # post request to the API endpoint to merge to pdf files
        response = requests.post(url,
        headers={
        "x-api-key": api_key
        },
        data={
        "url": files
        }
        )

    # checking if the request is successful or not
    if response.status_code == 200:
        print(response)
        response_json = response.json()
        print(response_json)
        file_url = response_json['url']
        print(file_url)
        pdf_to_json(file_url)
    else:
        tries = tries -1

    # sleep for some time
    time.sleep(0.5)
    print("request failed, trying again")
    print("request failed, returning")

# file's main function
def main():
    merge_files_output_JSON()

main()