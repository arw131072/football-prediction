CONTINENTAL_CHAMPIONSHIPS = {
    "UEFA Euro",
    "Copa América",
    "African Cup of Nations",
    "AFC Asian Cup",
    "Gold Cup",
    "Oceania Nations Cup",
}

REGIONAL_CHAMPIONSHIPS = {
    "AFF Championship",
    "ASEAN Championship",
    "Arab Cup",
    "CAFA Nations Cup",
    "CECAFA Cup",
    "CFU Caribbean Cup",
    "COSAFA Cup",
    "EAFF Championship",
    "Gulf Cup",
    "SAFF Cup",
    "UNCAF Cup",
    "UNIFFAC Cup",
    "UEFA Nations League",
    "CONCACAF Nations League",
}

MINOR_OFFICIAL_COMPETITIONS = {
    "AFC Challenge Cup",
    "AFC Solidarity Cup",
    "Afro-Asian Games",
    "Asian Games",
    "Baltic Cup",
    "CONCACAF Series",
    "CONMEBOL–UEFA Cup of Champions",
    "East Asian Games",
    "FIFA Series",
    "Intercontinental Cup",
    "Island Games",
    "Melanesia Cup",
    "Nations Cup",
    "Nordic Championship",
    "Pacific Games",
    "South Asian Games",
    "South Pacific Games",
    "South Pacific Mini Games",
    "Southeast Asian Games",
    "Viva World Cup",
    "World Unity Cup",
}

CONFEDERATIONS_CUP = {
    "Confederations Cup",
}

WORLD_CUP = {
    "FIFA World Cup",
}


def tournament_importance(tournament: str) -> float:
    """
    FIFA-inspired tournament importance weights.
    """

    name = tournament.lower()

    if tournament == "Friendly":
        return 10

    if (
        "qualification" in name
        or "qualifier" in name
        or "qualifiers" in name
    ):
        return 25

    if tournament in WORLD_CUP:
        return 50

    if tournament in CONFEDERATIONS_CUP:
        return 40

    if tournament in CONTINENTAL_CHAMPIONSHIPS:
        return 35

    if tournament in REGIONAL_CHAMPIONSHIPS:
        return 25

    if tournament in MINOR_OFFICIAL_COMPETITIONS:
        return 15

    # Invitational / exhibition tournaments
    return 15