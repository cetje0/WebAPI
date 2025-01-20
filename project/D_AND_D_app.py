import API_functies as api

while True:
    print(f"\n __________________________________________________________________")
    print(f" Welkom bij D&D, voor dat u begint moet u eerst u character maken")
    print(f"dit zijn de delen van u character:\n", "abiliy\n", "Alignment\n", "Background\n", "Language\n", "Proficiency\n", "Skill\n")
    keuze = input(f"met welke deel wilt u beginnen: ")

    if keuze.lower() == "ability":
        print(f"u kan kiezen uit:\n", "CHA: ")