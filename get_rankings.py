''' The purpose of this script is to fetch the most recent
    EC rankings fantasypros.com has to offer.'''
import urllib
import os


def get_ranks(scoring_is_ppr):
    ''' Simple function to update rankings.'''
    directory = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "Rankings")
    pre_url = "https://www.fantasypros.com/nfl/rankings/"
    post_url = "-cheatsheets?export=xls"
    position_tags = ["-rb", "-wr", "-te"]

    # QB rankings don't change between PPR and Standard scoring systems.
    download_link = "https://www.fantasypros.com/nfl/rankings/" \
                    "ppr-cheatsheets?export=xls"
    filename = os.path.join(directory, "OVERALL_PPR_RANKINGS.xls")
    urllib.urlretrieve(download_link, filename)
    download_link = "https://www.fantasypros.com/nfl/rankings/consensus" \
                    "-cheatsheets.php?export=xls"
    filename = os.path.join(directory, "OVERALL_RANKINGS.xls")
    urllib.urlretrieve(download_link, filename)
    download_link = "https://www.fantasypros.com/nfl/rankings/" \
                    "qb-cheatsheets.php?export=xls"
    filename = os.path.join(directory, "QB_RANKINGS.xls")
    urllib.urlretrieve(download_link, filename)

    if scoring_is_ppr:
        for position in position_tags:
            download_link = pre_url + "ppr"+position + post_url
            filename = os.path.join(directory,
                                    "PPR_"+position[1:].upper() +
                                    "_RANKINGS.xls")
            urllib.urlretrieve(download_link, filename)

    else:
        for position in position_tags:
            download_link = pre_url + position[1:] + post_url
            filename = os.path.join(directory,
                                    position[1:].upper() +
                                    "_RANKINGS.xls")
            urllib.urlretrieve(download_link, filename)

if __name__ == "__main__":
    get_ranks(True)
    get_ranks(False)
