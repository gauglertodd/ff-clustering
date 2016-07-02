''' The purpose of this script is to fetch the most recent
    EC rankings fantasypros.com has to offer.'''
import urllib


def get_ranks(scoring_is_ppr):
    ''' Simple function to update rankings.'''
    pre_url = "https://www.fantasypros.com/nfl/rankings/"
    post_url = "-cheatsheets?export=xls"
    position_tags = ["", "-rb", "-wr", "-te"]

    # QB rankings don't change between PPR and Standard scoring systems.
    download_link = "https://www.fantasypros.com/nfl/rankings/" \
                    "ppr-cheatsheets?export=xls"
    urllib.urlretrieve(download_link, "OVERALL_PPR_RANKINGS.xls")
    download_link = "https://www.fantasypros.com/nfl/rankings/consensus" \
                    "-cheatsheets.php?export=xls"
    urllib.urlretrieve(download_link, "OVERALL_RANKINGS.xls")

    if scoring_is_ppr:
        for position in position_tags:
            download_link = pre_url + "ppr"+position + post_url
            urllib.urlretrieve(download_link,
                               "PPR_"+position[1:].upper()+"_RANKINGS.xls")
    else:
        for position in position_tags:
            download_link = pre_url + position[1:] + post_url
            urllib.urlretrieve(download_link,
                               position[1:].upper()+"_RANKINGS.xls")

get_ranks(False)
