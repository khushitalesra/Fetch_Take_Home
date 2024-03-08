import requests, re

def get_data_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Unable to get data", response.status_code)
        return None

def grouping_items(input):
    item_dict = {}
    for i in input:
        if i.get('name'):
            list_id = i['listId']
            item_dict.setdefault(list_id, []).append(i)
    return item_dict

def sort_num(name):
    match = re.search(r'\d+', name)
    return int(match.group()) if match else float('inf')

def items_show(items_group):
    list_ids = sorted(items_group.keys())
    ind = 0

    while ind < len(list_ids):
        ids = list_ids[ind]
        print(f"List ID: {ids}")
        sort_by_name = sorted(items_group[ids], key=lambda x:sort_num(x['name']))
        for item in sort_by_name:
            print(f"  {item['id']}: {item['name']}")
        ind += 1


def main():
    url = "https://fetch-hiring.s3.amazonaws.com/hiring.json"
    input = get_data_from_url(url)
    if not input:
        return
    
    items_group = grouping_items(input)
    items_show(items_group)

if __name__ == "__main__":
    main()
