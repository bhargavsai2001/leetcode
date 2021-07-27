class Solution(object):

    def rankTeams(self, votes):

        """

        :type votes: List[str]

        :rtype: str

        """

        max_teams = 26

        all_teams = set(votes[0])

        num_voters = len(votes)

        votes_by_team = [[0 for _ in range(max_teams)] for _ in range(max_teams)]

        for vote in votes:

            for position, team in enumerate(vote):

                votes_by_team[ord(team) - ord('A')][position] -= 1

        votes_by_teams = [tuple(vote) + (index,) for index, vote in enumerate(votes_by_team)]

        votes_by_teams.sort()

        rank = []

        for result in votes_by_teams:

            team_char = chr(ord('A') + result[-1])

            if team_char in all_teams:

                rank.append(team_char)

        return ''.join(rank)