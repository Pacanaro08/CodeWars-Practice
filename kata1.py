# DESCRIPTION:

# Trilingual democracy
# Switzerland has four official languages: German, French, Italian, and Romansh.
# When native speakers of one or more of these languages meet, they follow certain regulations to choose a language for the group.2 Here are the rules for groups of exactly three people:
# When all three are native speakers of the same language, it also becomes their group's language.
# When two are native speakers of the same language, but the third person speaks a different language, all three will converse in the minority language.
# When native speakers of three different languages meet, they eschew these three languages and instead use the remaining of the four official languages.
# The languages are encoded by the letters D for Deutsch, F for Français, I for Italiano, and K for Rumantsch.
# Your task is to write a function that takes a list of three languages and returns the language the group should use.

# Examples:
# The language for a group of three native French speakers is French: FFF → F
# A group of two native Italian speakers and a Romansh speaker converses in Romansh: IIK → K
# When three people meet whose native languages are German, French, and Romansh, the group language is Italian: DFK → I


def trilingual_democracy(group):
    languages = ("D", "F", "I", "K")
    firstLetter = ""
    seccondLetter = ""
    thirdLetter = ""
    groupLanguage = ""
    for people in group:
        if firstLetter == "":
            firstLetter = people
        elif seccondLetter == "":
            seccondLetter = people
        else:
            thirdLetter = people
    
    if firstLetter == seccondLetter and seccondLetter == thirdLetter:
        groupLanguage = firstLetter
    elif firstLetter != seccondLetter and firstLetter != thirdLetter and seccondLetter != thirdLetter:
        for language in languages:
            if language not in group:
                groupLanguage = language
    else:
        if firstLetter == seccondLetter:
            groupLanguage = thirdLetter
        elif seccondLetter == thirdLetter:
            groupLanguage = firstLetter
        else:
            groupLanguage = seccondLetter



    print(groupLanguage)

group = input('Create the Group of People Using 3 Words (D, F, I or K):')
trilingual_democracy(group)
