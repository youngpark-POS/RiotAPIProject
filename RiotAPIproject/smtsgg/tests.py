from django.test import TestCase

from .riotapi import get_puuid, get_match_ids, get_single_match, get_summoner_id_encrypted, get_rank_info

# Create your tests here.

class RiotAPITest(TestCase):
    def invalid_username_test(self):
        id = "nojqwegjnr"
        tag = "957"
        self.assertIs(get_puuid(id, tag), KeyError)