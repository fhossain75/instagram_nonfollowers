import re


def clean_usernames(file_name):
    """
    Cleans a list of usernames from a file.
    Manual copying usernames from instagram following/follower tab includes additional text like name & profile picture.

    This function reads a file containing social media usernames, one per line, and returns a list of usernames. It
    filters out any line that does not match a simple username pattern (alphanumeric, underscore, and period
    characters only) and ignores lines with single characters.

    Note: Additional text, such as names, might pass through the filtering process and be included in the returned list.

    :param file_name: The name of the file to read from.
    :return: A list of usernames.
    """

    pattern = re.compile(r'^[\w.]+$')
    usernames = []

    try:
        with open(file_name, 'r') as file:
            for line in file:
                username = line.strip()
                if pattern.match(username) and len(username) > 1:
                    usernames.append(username)
    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")
    except IOError:
        print(f"Error: Could not read the file {file_name}.")

    return usernames


# Main usage of the functions
if __name__ == "__main__":
    followers = set(clean_usernames('followers.txt'))
    following = set(clean_usernames('following.txt'))

    # Non-followers calculation
    non_followers = following - followers

    print("Followers:", len(followers))
    print("Following:", len(following))
    print("Non-Followers:", len(non_followers))
    print(non_followers)
