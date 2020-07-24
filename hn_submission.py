from operator import itemgetter
import requests
from plotly.graph_objs import Bar
from plotly import offline


# * Make API call and store the responce data
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
req = requests.get(url)
print(f"Status code: {req.status_code}")


# * Process information about each submission
submission_ids = req.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    req = requests.get(url)
    print(f"id: {submission_id}\tstatus: {req.status_code}")
    responce_dict = req.json()
    # Buils a dictionary for each article
    submission_dict = {
        "title": responce_dict["title"],
        "hn_link": f"https://news.ycombinator.com/item?id={submission_id}",
        "comments": responce_dict.get("descendants", 0),
    }
    # Appends to list
    submission_dicts.append(submission_dict)
print(submission_dicts)
submission_dicts = sorted(submission_dicts,
                          key=itemgetter("comments"), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")


# * Data Visualization
discussions_links, comments, labels = [], [], []
for submission in submission_dicts:
  # creates link with label
    labels.append(submission["title"])
    comments.append(submission["comments"])
    # creates link tag
    label = submission["title"]
    link = submission["hn_link"]
    a = f"<a href='{link}'>{label}</a>"
    # appends new link to list
    discussions_links.append(a)
# Provides data for X and Y values |X title and Y comments|
data = [{
    "type": "bar",
    "x": discussions_links,
    "y": comments,
    "hovertext": labels,
    "marker": {
        "color": "rgb(60,100,150)",
        "line": {"width": 1.5, "color": "rgb(25,25,25)"}
    },
    "opacity": 0.6,
}]

layout = {
    "title": "Hacker News Trending Discussions",
    "titlefont": {"size": 28},
    "xaxis": {'title': 'Discussions',
              "titlefont": {"size": 24},
              "tickfont": {"size": 14}},
    "yaxis": {'title': 'Comments',
              "titlefont": {"size": 24},
              "tickfont": {"size": 14}},
}

fig = {"data": data, "layout": layout}
offline.plot(fig, filename="hn_submission.html")
