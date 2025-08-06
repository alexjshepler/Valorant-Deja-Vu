import requests
import json

GET_ALL_MATCHES_HAR = './Get_All_Matches.har'
GET_ONE_MATCH_HAR = './Get_One_Match.har'


def extract_requests_from_har(har_file_path):
    with open(har_file_path, "r", encoding="utf-8") as f:
        har_data = json.load(f)

    requests_data = []

    for entry in har_data["log"]["entries"]:
        request = entry["request"]
        response = entry.get("response", {})

        request_data = {
            "method": request["method"],
            "url": request["url"],
            "headers": {h["name"]: h["value"] for h in request["headers"]},
            "cookies": {c["name"]: c["value"] for c in request.get("cookies", [])},
            "query_params": {
                p["name"]: p["value"] for p in request.get("queryString", [])
            },
            "post_data": request.get("postData", {}).get("text", ""),
            "response_status": response.get("status", None),
            "response_content": response.get("content", {}).get("text", ""),
        }

        requests_data.append(request_data)

    return requests_data


def replay_request(request_data):
    method = request_data["method"].lower()
    url = request_data["url"]
    headers = request_data["headers"]
    data = request_data["post_data"] if request_data["post_data"] else None

    session = requests.Session()

    # Add cookies if present
    if request_data["cookies"]:
        session.cookies.update(request_data["cookies"])

    # Make the request
    response = getattr(session, method)(url, headers=headers, data=data)

    return response


def get_matches():
    pass

def get_match(id):
    pass

def main():
    get_match()

if __name__ == '__main__':
    main()
