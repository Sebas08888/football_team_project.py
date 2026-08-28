from Player import Player
from Coach import Coach
from FootballTeam import FootballTeam
from League import League
from ClubTeam import ClubTeam
from Match import Match
from Stadium import Stadium

if __name__ == "__main__":

    # Player
    player1 = Player("Cristiano", 41, "Delantero")
    player2 = Player("Mbappe", 27, "Delantero")
    player3 = Player("Olise", 24, "Extremo")
    player4 = Player("Rodri", 30, "Mediocampista")
    player5 = Player("Anderson", 23, "Mediocampista")  
    player6 = Player("Vinicius", 25, "Delantero")      

    # Reto 3 - Coach
    coach1 = Coach("Mourinho", 20)
    coach2 = Coach("Flick", 10)
    coach1.give_instructions("4-3-3")
    coach2.give_instructions("4-2-3-1")

    # Reto 4 - Equipos y jugadores
    team1 = ClubTeam("Real Madrid", trophies=15)
    team1.hire_coach(coach1)
    team1.sign_player(player6)   # Vinicius
    team1.sign_player(player2)   # Mbappe
    team1.sign_player(player3)   # Olise
    team1.show_team()

    team2 = ClubTeam("Barcelona", trophies=10)
    team2.hire_coach(coach2)
    team2.sign_player(Player("Yamal", 17, "Extremo"))
    team2.sign_player(player4)   # Rodri
    team2.show_team()

    # Reto 6 - Manchester City y Liverpool
    club3 = ClubTeam("Manchester City", trophies=10)
    club4 = ClubTeam("Liverpool", trophies=6)
    player7 = Player("Haaland", 23, "Delantero")
    club3.sign_player(player7)
    club3.sign_player(player5)   # Anderson

    # Reto 9 - Estadios
    stadium1 = Stadium("Santiago Bernabeu", 81000, "Madrid")
    stadium2 = Stadium("Spotify Camp Nou", 99000, "Barcelona")
    stadium3 = Stadium("Etihad Stadium", 55000, "Manchester")
    team1.assign_stadium(stadium1)
    team2.assign_stadium(stadium2)
    club3.assign_stadium(stadium3)
    print(stadium1)
    print(stadium2)
    print(stadium3)

    # Reto 1 - Goles
    player1.score()
    player1.score()
    player2.score()

    # Reto 2 - Transferencias
    player1.transfer("Al Nassr")
    player3.transfer("Real Madrid")

    # Reto 5 - Liga con todos los equipos al final
    league = League("")
    league.add_team(team1)
    league.add_team(team2)
    league.add_team(club3)
    league.add_team(club4)
    league.show_classification()

    # Reto 7 - Partido
    match1 = Match(team1, team2)
    match1.play()

    # Reto 8 - Comparar trofeos
    team1.compare_trophies(team2)

    # Reto 10 - Retiro de Cristiano
    player1.retire(final_goals=1000)