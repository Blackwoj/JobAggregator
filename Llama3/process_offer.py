import json
from main import get_response

with open('../../scrapped/scrap.bulldog_jobs.json', 'r', encoding="utf8") as file:
    data = json.load(file)

processed_offers = []
for i, x in enumerate(data):
    job_description = x['htmlData']
    print(i, x['_id'])

    try:
        response = get_response(job_description)

        response_clear = response.replace('\n', '')
        response_clear = response_clear.replace("\\", '')
        print(response_clear)
        response_object = {
            "_id": {
                '$oid': x['_id']['$oid']
            },
            "data": response_clear
        }
        processed_offers.append(response_object)

        print(response)
    except:
        print('ERROR')
        break


try:
    with open('.output.json', 'w+') as json_file:
        json.dump(processed_offers, json_file, indent=4)
    print("All processed offers saved to 'output.json'")
except Exception as e:
    print(f"Failed to write to file: {str(e)}")