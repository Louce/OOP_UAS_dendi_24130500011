# OOP_UAS1_dendi_24130500011.py

from datetime import date
from abc import ABC, abstractmethod

# ==============================================================================
# 1. DEFINISI KELAS BERDASARKAN UML DIAGRAM
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
                 jerseyNumber: int, marketValue: float, position: str, status: str = "Active"):
        super().__init__(personId, firstName, lastName, dateOfBirth, nationality)
        self._jerseyNumber = jerseyNumber
        self._marketValue = marketValue
        self._position = position
        self._status = status
        # teamId akan di-set ketika pemain ditambahkan ke tim
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
                 licenseLevel: str, role: str):
        super().__init__(personId, firstName, lastName, dateOfBirth, nationality)
        self._licenseLevel = licenseLevel
        self._role = role
        # teamId akan di-set ketika pelatih ditugaskan ke tim
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
                 department: str, role: str):
        super().__init__(personId, firstName, lastName, dateOfBirth, nationality)
        self._department = department
        self._role = role
        # clubId akan di-set ketika staf dipekerjakan oleh klub
        self._clubId = None

    def performDuties(self):
        print(f"Staff {self.getFullName()} ({self._role}) is performing duties.")

    def __str__(self):
        return f"Staff: {self.getFullName()} ({self._role}, Dept: {self._department})"

class Team:
    """Kelas untuk merepresentasikan tim dalam sebuah klub."""
    def __init__(self, teamId: str, name: str, league: str, division: str):
        self._teamId = teamId
        self._name = name
        self._league = league
        self._division = division
        self._players = []
        self._coaches = []
        # clubId akan di-set ketika tim ditambahkan ke klub
        self._clubId = None

    def addPlayer(self, player: Player):
        if player not in self._players:
            self._players.append(player)
            player._teamId = self._teamId
            print(f"{player.getFullName()} has been added to team {self._name}.")

    def removePlayer(self, player: Player):
        if player in self._players:
            self._players.remove(player)
            player._teamId = None
            print(f"{player.getFullName()} has been removed from team {self._name}.")
    
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
    """Kelas untuk merepresentasikan klub sepak bola."""
    def __init__(self, clubId: str, name: str, foundingDate: date, league: str):
        self._clubId = clubId
        self._name = name
        self._foundingDate = foundingDate
        self._league = league
        self._teams = []
        self._staff = []
        self._stadium = None # Relasi 1-ke-1

    def addTeam(self, team: Team):
        if team not in self._teams:
            self._teams.append(team)
            team._clubId = self._clubId
            print(f"Team {team._name} is now managed by {self._name}.")
    
    def setStadium(self, stadium):
        self._stadium = stadium
        print(f"Stadium {stadium._name} is now the home of {self._name}.")

    def display_info(self):
        print(f"\n===== Club Information: {self._name} =====")
        print(f"Founded: {self._foundingDate}")
        print(f"League: {self._league}")
        if self._stadium:
            print(f"Home Stadium: {self._stadium._name}")
        
        print("\nTeams:")
        for team in self._teams:
            print(f"  - {team._name} ({team._league})")
        print("=========================================")

# Kelas lain yang tidak digunakan langsung di skenario, tapi didefinisikan
# sesuai diagram untuk kelengkapan.
class Stadium:
    def __init__(self, stadiumId: str, name: str, capacity: int, address: str):
        self._stadiumId = stadiumId
        self._name = name
        self._capacity = capacity
        self._address = address

# ==============================================================================
# 2. IMPLEMENTASI SKENARIO FC CAKRAWALA
# ==============================================================================
if __name__ == "__main__":
    print("--- Starting Club Initialization ---")

    # Membuat Klub
    fc_cakrawala = Club(
        clubId="FCC-01", 
        name="FC Cakrawala", 
        foundingDate=date(2020, 1, 10),
        league="Liga Universitas"
    )

    # Membuat Tim U-23
    fc_cakrawala_muda = Team(
        teamId="FCCM-U23-01", 
        name="FC Cakrawala Muda", 
        league="Liga Universitas", 
        division="U-23"
    )

    # Menambahkan tim ke klub
    fc_cakrawala.addTeam(fc_cakrawala_muda)
    
    # Membuat dan menugaskan pelatih ke tim
    head_coach = Coach(
        personId="P-001", firstName="Budi", lastName="Santoso", dateOfBirth=date(1980, 5, 15),
        nationality="Indonesia", licenseLevel="AFC Pro", role="Head Coach"
    )
    
    assistant_coach = Coach(
        personId="P-002", firstName="Citra", lastName="Dewi", dateOfBirth=date(1985, 8, 20),
        nationality="Indonesia", licenseLevel="AFC A", role="Assistant Coach"
    )
    
    fc_cakrawala_muda.addCoach(head_coach)
    fc_cakrawala_muda.addCoach(assistant_coach)
    
    # Membuat 15 pemain dan menambahkannya ke tim
    # (data pemain disederhanakan untuk contoh)
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
        player = Player(
            personId=f"P-{100+i}",
            firstName=p_data[0],
            lastName=p_data[1],
            dateOfBirth=date(2002, 1, 1),
            nationality="Indonesia",
            jerseyNumber=p_data[2],
            marketValue=10000.0,
            position=p_data[3]
        )
        fc_cakrawala_muda.addPlayer(player)
        
    # Menampilkan informasi hasil inisialisasi
    fc_cakrawala.display_info()
    fc_cakrawala_muda.display_roster()