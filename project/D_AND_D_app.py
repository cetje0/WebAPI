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
        print(f"_______________________________________\n")
        print(f"{info_ability}\n")
        print(f"_______________________________________\n",
              f"These are the skills of the ability\n")

        for skill in skills:
            print(skill['name'])

    if keuze.lower() == "alignment":
        alignments = api.D_D_ALLE_alignments()
        for alignment in alignments:
            print(alignment["name"])
        alignment_keuze = input(f"over welke alignment wilt u meer weten? ")
        controle = api.D_D_alignments_info(alignment_keuze)
        info_alignment = api.D_D_alignments_info(alignment_keuze)
        print(info_alignment)
        if controle == False:
            print("You have to select a choice from above")
            continue 
    
    if keuze.lower() == "language":
        languages = api.D_D_language()
        print(f"\ndit zijn de talen",
              f"\n_______________________________________________")
        for language in languages:
            print(language["name"])
        language_keuze = input(f"over welke taal wil je meer weten? ")
        print(api.D_D_language_info(language_keuze))
        