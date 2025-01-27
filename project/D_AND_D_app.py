import API_functies as api

while True:
    print(f"\n __________________________________________________________________")
    print(f" Welkom bij D&D, voor dat u begint moet u eerst u character maken")
    print(f"dit zijn de delen van u character:\n", "ability\n", "Alignment\n", "Background\n", "Language\n", "Proficiency\n", "Skill\n")
    keuze = input(f"met welke deel wilt u beginnen: ")

    if keuze.lower() == "ability":
        print(f"CHA: uitstraling\n",
              "CON: constructie\n",
              "DEX: behendigheid\n",
              "INT: intelligents\n",
              "STR: kracht\n",
              "WIS: wijsheid\n")
        ability_keuze = input(f"over welke zo je meer willen weten?") 
        skills = api.D_D_abilitys(ability_keuze)
        if skills == False:
            print("You have to select a choice from above")
            continue
        info_ability = api.D_D_abilitys_info(ability_keuze)
        print(f"{info_ability}\n")
        print(f"_______________________________________\n",
              f"These are the skills of the ability\n")

        for skill in skills:
            print(skill['name'])
        