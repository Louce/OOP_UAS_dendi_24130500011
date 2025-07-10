# OOP_UAS3_dendi_24130500011.py

from datetime import date
from abc import ABC, abstractmethod

# ==============================================================================
# 1. DEFINISI KELAS (Sama seperti sebelumnya)
# ==============================================================================

class Person(ABC):
    """Kelas abstract untuk semua individu dalam klub."""
    def __init__(self, personId: str, firstName: str, lastName: str, dateOfBirth: date, nationality: str):
        self._personId = personId
        self._firstName = firstName
        self._lastName = lastName
        self._dateOfBirth = dateOfBirth
        self._nationality = nationality

    def getFullName(self) -> str:
        return f"{self._firstName} {self._lastName}"

    @abstractmethod
    def __str__(self):
        pass

class Player(Person):
    """Kelas untuk merepresentasikan pemain."""
    def __init__(self, personId: str, firstName: str, lastName: str, dateOfBirth: date, nationality: str, 
                 jerseyNumber: int, marketValue: float, position: str, status: str = "Active", **kwargs):
        super().__init__(personId, firstName, lastName, dateOfBirth, nationality)
        self._jerseyNumber = jerseyNumber
        self._marketValue = marketValue
        self._position = position
        self._status = status
        self._teamId = None 

    def train(self):
        print(f"Player {self.getFullName()} is training.")

    def playMatch(self):
        print(f"Player {self.getFullName()} is playing a match.")
        
    def __str__(self):
        return f"Player: {self.getFullName()} (#{self._jerseyNumber}, {self._position})"

class Coach(Person):
    """Kelas untuk merepresentasikan pelatih."""
    def __init__(self, personId: str, firstName: str, lastName: str, dateOfBirth: date, nationality: str, 
                 licenseLevel: str, role: str, **kwargs):
        super().__init__(personId, firstName, lastName, dateOfBirth, nationality)
        self._licenseLevel = licenseLevel
        self._role = role
        self._teamId = None

    def conductTraining(self):
        print(f"Coach {self.getFullName()} ({self._role}) is conducting training.")

    def selectSquad(self):
        print(f"Coach {self.getFullName()} is selecting the squad.")

    def __str__(self):
        return f"Coach: {self.getFullName()} ({self._role}, License: {self._licenseLevel})"

class Staff(Person):
    """Kelas untuk merepresentasikan staf klub lainnya."""
    def __init__(self, personId: str, firstName: str, lastName: str, dateOfBirth: date, nationality: str, 
                 department: str, role: str, **kwargs):
        super().__init__(personId, firstName, lastName, dateOfBirth, nationality)
        self._department = department
        self._role = role
        self._clubId = None

    def performDuties(self):
        print(f"Staff {self.getFullName()} ({self._role}) is performing duties.")

    def __str__(self):
        return f"Staff: {self.getFullName()} ({self._role}, Dept: {self._department})"

# ==============================================================================
# 2. IMPLEMENTASI FACTORY METHOD PATTERN
# ==============================================================================

class PersonFactory:
    """
    Factory class untuk membuat objek turunan dari Person.
    Ini adalah implementasi sederhana dari Factory Method Pattern.
    """
    @staticmethod
    def createPerson(type: str, *args, **kwargs):
        """
        Membuat objek Person berdasarkan tipe yang diberikan.
        :param type: Tipe person ('player', 'coach', 'staff').
        :param args: Argumen posisional untuk constructor.
        :param kwargs: Argumen keyword untuk constructor.
        :return: Instance dari Player, Coach, atau Staff.
        """
        type = type.lower()
        if type == 'player':
            return Player(*args, **kwargs)
        elif type == 'coach':
            return Coach(*args, **kwargs)
        elif type == 'staff':
            return Staff(*args, **kwargs)
        else:
            raise ValueError(f"Tipe person '{type}' tidak valid.")

# Kelas Team dan Club tetap sama
class Team:
    def __init__(self, teamId: str, name: str, league: str, division: str):
        self._teamId = teamId
        self._name = name
        self._league = league
        self._division = division
        self._players = []
        self._coaches = []
        self._clubId = None

    def addPlayer(self, player: Player):
        if player not in self._players:
            self._players.append(player)
            player._teamId = self._teamId
            print(f"{player.getFullName()} has been added to team {self._name}.")

    def addCoach(self, coach: Coach):
        if coach not in self._coaches:
            self._coaches.append(coach)
            coach._teamId = self._teamId
            print(f"{coach.getFullName()} ({coach._role}) has been assigned to team {self._name}.")
            
    def display_roster(self):
        print(f"\n--- Roster for {self._name} ---")
        print("Coaches:")
        for coach in self._coaches:
            print(f"  - {coach}")
        print("\nPlayers:")
        for player in self._players:
            print(f"  - {player}")
        print("---------------------------------")


class Club:
    def __init__(self, clubId: str, name: str, foundingDate: date, league: str):
        self._clubId = clubId
        self._name = name
        self._foundingDate = foundingDate
        self._league = league
        self._teams = []
        self._staff = []
        self._stadium = None

    def addTeam(self, team: Team):
        if team not in self._teams:
            self._teams.append(team)
            team._clubId = self._clubId
            print(f"Team {team._name} is now managed by {self._name}.")

    def display_info(self):
        print(f"\n===== Club Information: {self._name} =====")
        print(f"Founded: {self._foundingDate}")
        print(f"League: {self._league}")
        print("\nTeams:")
        for team in self._teams:
            print(f"  - {team._name} ({team._league})")
        print("=========================================")

# ==============================================================================
# 3. IMPLEMENTASI SKENARIO MENGGUNAKAN FACTORY
# ==============================================================================
if __name__ == "__main__":
    print("--- Starting Club Initialization (using Factory Method) ---")

    # Membuat Klub dan Tim (tidak berubah)
    fc_cakrawala = Club("FCC-01", "FC Cakrawala", date(2020, 1, 10), "Liga Universitas")
    fc_cakrawala_muda = Team("FCCM-U23-01", "FC Cakrawala Muda", "Liga Universitas", "U-23")
    fc_cakrawala.addTeam(fc_cakrawala_muda)
    
    # Membuat dan menugaskan pelatih ke tim MENGGUNAKAN FACTORY
    head_coach = PersonFactory.createPerson(
        'coach',
        personId="P-001", firstName="Budi", lastName="Santoso", dateOfBirth=date(1980, 5, 15),
        nationality="Indonesia", licenseLevel="AFC Pro", role="Head Coach"
    )
    
    assistant_coach = PersonFactory.createPerson(
        'coach',
        personId="P-002", firstName="Citra", lastName="Dewi", dateOfBirth=date(1985, 8, 20),
        nationality="Indonesia", licenseLevel="AFC A", role="Assistant Coach"
    )
    
    fc_cakrawala_muda.addCoach(head_coach)
    fc_cakrawala_muda.addCoach(assistant_coach)
    
    # Membuat 15 pemain dan menambahkannya ke tim MENGGUNAKAN FACTORY
    players_data = [
        ("Adi", "Nugroho", 10, "Forward"), ("Bambang", "Wijoyo", 7, "Midfielder"),
        ("Candra", "Kusuma", 4, "Defender"), ("Dedi", "Pratama", 1, "Goalkeeper"),
        ("Eka", "Saputra", 11, "Forward"), ("Fajar", "Maulana", 8, "Midfielder"),
        ("Gilang", "Ramadhan", 5, "Defender"), ("Hadi", "Purnomo", 2, "Defender"),
        ("Indra", "Gunawan", 6, "Midfielder"), ("Joko", "Susilo", 9, "Forward"),
        ("Kurniawan", "Dwi", 3, "Defender"), ("Leo", "Sihombing", 12, "Midfielder"),
        ("Mega", "Putra", 15, "Midfielder"), ("Nanda", "Setiawan", 14, "Defender"),
        ("Oscar", "Wibowo", 13, "Forward")
    ]

    for i, p_data in enumerate(players_data):
        player_args = {
            "personId": f"P-{100+i}",
            "firstName": p_data[0],
            "lastName": p_data[1],
            "dateOfBirth": date(2002, 1, 1),
            "nationality": "Indonesia",
            "jerseyNumber": p_data[2],
            "marketValue": 10000.0,
            "position": p_data[3]
        }
        player = PersonFactory.createPerson('player', **player_args)
        fc_cakrawala_muda.addPlayer(player)
        
    # Menampilkan informasi hasil inisialisasi
    fc_cakrawala.display_info()
    fc_cakrawala_muda.display_roster()