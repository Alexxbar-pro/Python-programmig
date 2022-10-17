from instapy import InstaPy
from instapy import smart_run

insta_username = 'user'
insta_password = 'pass'

session = InstaPy(username=insta_username, password=insta_password, headless_browser=False)

with smart_run(session):

    session.set_relationship_bounds(enabled=True, delimit_by_numbers=True, max_followers=4000, min_followers=45, min_following=77)

    session.set_dont_include(["friend1", "friend2", "friend3"])
    session.set_dont_like(["pizza", "#store"])

    session.like_by_tags(["programming", "hacking", "Tecnology"], amount=10)

    session.set_dont_like(["girls", "women", "sexi"])

    session.set_do_follow(True, percentage=60)

    session.set_do_comment(True, percentage=60)

    session.set_comments(["Very nice!", "Good", "Cool", "Very interesting", "Nice", "Interesting", "Nice job"])