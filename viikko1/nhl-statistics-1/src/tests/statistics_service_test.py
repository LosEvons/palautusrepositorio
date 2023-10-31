import unittest
from player import Player
from statistics_service import (
    StatisticsService, 
    sort_by_points, sort_by_assists, sort_by_goals,
    SortBy
)


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Jaakko", "Espoo", 4, 14),
            Player("Tiina", "Helsinki", 2, 12),
            Player("Riley", "Kouvola", 5, 15),
            Player("James", "Vantaa", 3, 13),
            Player("Alex", "Vantaa", 1, 11),
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService( PlayerReaderStub() )
        
    def test_sort_returns_points(self):
        self.assertEqual(sort_by_points(self.stats.search("Jaakko")), 18)
    def test_sort_returns_goals(self):
        self.assertEqual(sort_by_goals(self.stats.search("Jaakko")), 4)
    def test_sort_returns_assists(self):
        self.assertEqual(sort_by_assists(self.stats.search("Jaakko")), 14)
    
    def test_search_not_found(self):
        self.assertEqual(self.stats.search("Teppo"), None)
        
    def test_team_finds_players(self):
        vantaa_players = self.stats.team("Vantaa")
        self.assertEqual(len(vantaa_players), 2)
        for player in vantaa_players:
            self.assertEqual(player.team, "Vantaa")
            
    def test_top_orders_players(self):
        for e in SortBy:
            sorted_players = self.stats.top(4, e)
            top_player = sorted_players[0]
            for player in sorted_players:
                self.assertLessEqual(sort_by_points(player), sort_by_points(top_player))
            
        