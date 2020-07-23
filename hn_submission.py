from operator import itemgetter
import requests

# make API call and store the responce data
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
req = requests.get(url)
print(f"Status code: {req.status_code}")


# process information about each submission
submission_ids = req.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission
    url = "https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    req = requests.get(url)
    print(f"id: {submission_id}\tstatus: {req.status_code}")
    reponce_dict = req.json()
    # Buils a dictionary for each article
    submission_dict = {
        "title": reponce_dict,
        "hn_link": f"https://news.ycombinator.com/item?id={submission_id}",
        "comments": responce_dict["desendants"],
    }
    # Appends to list
    submission_dicts.append(submission_dict)

submission_dicts - sorted(submission_dicts,
                          key=itemgetter("comments"), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
