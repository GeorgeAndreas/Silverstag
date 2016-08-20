# Center Hub (1.0) by Windyplains

strings = [
###########################################################################################################################
#####                                                COMMON STRINGS                                                   #####
###########################################################################################################################
	("hub_done",                  "Done"),
	("hub_general_info",          "General Info"),
	("hub_finances",              "Finances"),
	("hub_improvements",          "Improvements"),
	("hub_recruitment",           "Recruitment"),
	("hub_advisors",              "Advisors"),
	("hub_quests",                "Quests"),
	("hub_garrison",              "Garrison"),
	("hub_s21",                   "{s21}"),
	("hub_s22",                   "{s22}"),
	("hub_r21",                   "{reg21}"),
	("hub_general_label",         "Information about {s21}:"),
	("hub_prosperity",            "Prosperity:  {reg21}"),
	("hub_relation",              "Relation:  {reg21}"),
	("hub_culture",               "Culture:  {s21}"),
	("hub_recovery_state",        " * Recovery Progress:  {reg21}%"),
	("hub_recruitment_rating",    "Recruitment Rating:  {reg1}"),
	("hub_recruitment_bound",     " * Recruitment Rating of {s21}:  {reg1}"),
	("hub_tariffs",               "Accumulated Tariffs: {reg21} denars"),
	("hub_r21_denars",            "{reg21} denars"),
	("hub_last_owner",            "{s22} was last held by {s21}"),
	("hub_improvement_s0",        "Improvement ({s0})"),
	("hub_incomes",               "Incomes:"),
	("hub_expenses",              "Expenses:"),
	("hub_income_prisoners",      "Prisoner Caravans"),
	("hub_income_rent",           "Center Income"),
	("hub_income_tariffs",        "Trade Tariffs"),
	("hub_improvement",           " * {s21}"),
	("hub_expense_recruitment",   "Garrison Recruitment"),
	("hub_expense_training",      "Garrison Training"),
	("hub_expense_patrols",       "Regional Patrols"),
	("hub_expense_patrol_no",     " * Patrol #{reg21}"),
	("hub_improvement_upkeep",    "{reg21} denars per week"),
	("hub_improvement_percent",   "{reg21}%"),
	("hub_treasury",              "Treasury:"),
	("hub_treasury_income",       "Treasury Allocation"),
	("hub_treasury_balance",      "Treasury Balance"),
	("hub_treasury_projection",   "Treasury Projection"),
	("hub_investments",           "Investments:"),
	("hub_total",                 "Totals:"),
	("hub_expense_wages",         "Garrison Wages"),
	("hub_net_change",            "Net Change"),
	("hub_button_deposit",        "Deposit"),
	("hub_button_withdrawal",     "Withdraw"),
	("hub_button_increase",       "+250"),
	("hub_button_decrease",       "-250"),
	("hub_button_allocation",     "Allocation"),
	("hub_button_dismiss",        "Dismiss"),
	("hub_label_treasury",        "Castle Treasury"),
	("hub_label_treasury_value",  "Transfer {reg21} Denars"),
	("hub_label_starred",         "Note: Items denoted with a * are already included in their parent category."),
	("hub_label_construction",    "This page is still being constructed.  It is blank for a reason."),
	("hub_title_recruitment",     "Recruitment Options"),
	("hub_button_recruit",        "Recruit Troop"),
	("hub_button_inspect_gear",   "Inspect Equipment"),
	("hub_button_dismiss",        "Dismiss Troop"),
	("hub_label_bound_ratings",   "Recruitment Rating for Bound Villages:"),
	("hub_rec_rate_type",         " * All ratings multiplied by {reg31} due to being a {s31}."),
	("hub_rec_rate_prosperity",   " * + {reg32} due to a prosperity rating of {reg42}."),
	("hub_rec_rate_distance",     " * + {reg33} due to a distance of {reg43} from the village's bound center."),
	("hub_rec_rate_cotg_pers",    " * + {reg34} due to {s32}'s persuasion score of {reg44}."),
	("hub_rec_rate_cotg_renown",  " * + {reg35} due to {s32}'s renown score of {reg45}."),
	("hub_rec_rate_player_renown"," * + {reg36} due to {s33}'s renown score of {reg46}."),
	("hub_rec_rate_faction",      " * + {reg37} due to the faction's recruitment setting of {reg47}."),
	("hub_rec_rate_difficulty",   " * + {reg38} due to the game's difficulty setting."),
	("hub_rec_rate_conscription", " * + {reg39} due to mandatory conscription."),
	("hub_rec_rate_no_rating",    "This center cannot currently be recruited from."),
	("hub_village_looted",        " * Recruitment Rating of {s21}:  Looted."),
	("hub_village_raiding",       " * Recruitment Rating of {s21}:  Being raided."),
	("hub_village_infested",      " * Recruitment Rating of {s21}:  Infested."),
	("hub_general_stats",         "General Statistics:"),
	("hub_troop_prereqs",         "Recruitment Requirements:"),
	("hub_desc_armor_value",      "Armor Rating: {reg21}"),
	("hub_desc_melee_value",      "Melee Rating: {reg21}"),
	("hub_desc_ranged_value",     "Ranged Rating: {reg21}"),
	("hub_prereq_mounted",        "Stables"),
	("hub_prereq_armored",        "Blacksmith"),
	("hub_prereq_elite",          "Training Ground"),
	("hub_prereq_ranged",         "Fletcher's Workshop"),
	("hub_no_range",              "Ranged Rating: None"),
	("hub_available_nobles",      "Veterans: {reg21}"),
	("hub_available_peasants",    "Peasants: {reg21}"),
	("hub_available_mercenaries", "Mercenaries: {reg21}"),
	("hub_available_mounts",      "Mounts: {reg21}"),
	("hub_prereq_peasant",        "Peasant Recruit"),
	("hub_prereq_noble",          "Veteran Recruit"),
	("hub_prereq_mercenary",      "Mercenary Recruit"),
	("hub_prereq_mount",          "Mount"),
	("hub_troop_count",           "{reg21} in Service"),
	("hub_note_shift_multiplies", "Note: Holding down the SHIFT key hires or dismisses in multiples of 10."),
	("hub_faction_troop_wages",   " * Kingdom Setting: Troop Wages"),
	("hub_faction_center_income", " * Kingdom Setting: Center Income"),
	("hub_faction_tariff_income", " * Kingdom Setting: Tariff Income"),
	("hub_info_being_raided",     "Village is being raided."),
	("hub_info_looted",           "Village has been looted."),
	("hub_info_bandits",          "Village is infested with bandits."),
	("hub_improvement_building",  " * Currently {s2} is being constructed."),
	("hub_current_construction",  "Current Construction:"),
	("hub_title_infrastructure",  "Infrastructure"),
	("hub_current_improvements",  "Current Improvements:"),
	("hub_improvement_name",      " * {s0}{s11}"),
	("hub_build_cancel",          "Cancel"),
	("hub_build_days_left",       "{reg21} day{reg22?s:} left of {reg23} days"),
	("hub_build_time",            "This improvement takes {reg2} day{reg3?s:} to complete."),
	("hub_build_cost",            "This improvement costs {reg21} denars."),
	("hub_button_build",          "Build"),
	("hub_button_repair",         "Repair"),
	("hub_button_destroy",        "Destroy"),
	("hub_build_time_done",       "This improvement is already built."),
	("hub_build_cost_done",       " "),
	("hub_center_type_vct",       "Applicable: Towns, Castles & Villages"),
	("hub_center_type_v",         "Applicable: Villages"),
	("hub_center_type_c",         "Applicable: Castles"),
	("hub_center_type_t",         "Applicable: Towns"),
	("hub_center_type_ct",        "Applicable: Towns & Castles"),
	("hub_center_type_vt",        "Applicable: Towns & Villages"),
	("hub_center_type_vc",        "Applicable: Castles & Villages"),
	("hub_troop_cost_modified",   "{reg21} denars{s22}"),
	("hub_improvement_empty",     "(empty)"),
	("hub_player_gold",           "Player: {reg21}"),
	("hub_improvements_caps",     "IMPROVEMENTS"),
	("hub_treasury_gold",         "Treasury: {reg21}"),
	("hub_town_lord",             "{s22} lord:  {s21}"),
	("hub_village_owner",         "Owned by {s21}"),
	("hub_center_rename",         "Rename Location"),
	("hub_prereq_center_relation","Center Relation of {reg21}+"),
	("hub_prereq_owner_only",     "You must be lord of this center"),
	("hub_prereq_affiliated",     "Affiliation: {s21}"),
	("hub_prereq_expensive",      "Recruitment cost is double as usual"),
	("hub_prereq_disreputable",   "Recruitment may tarnish your reputation"),
	
	## ORIGINAL CENTER NAMES
	### TOWNS BEGIN ###
	("hub_zendar",                "Zendar"),
	("hub_town_1",                "Sargoth"),
	("hub_town_2",                "Tihr"),
	("hub_town_3",                "Veluca"),
	("hub_town_4",                "Suno"),
	("hub_town_5",                "Jelkala"),
	("hub_town_6",                "Praven"),
	("hub_town_7",                "Uxkhal"),
	("hub_town_8",                "Reyvadin"),
	("hub_town_9",                "Khudan"),
	("hub_town_10",               "Tulga"),
	("hub_town_11",               "Curaw"),
	("hub_town_12",               "Wercheg"),
	("hub_town_13",               "Rivacheg"),
	("hub_town_14",               "Halmar"),
	("hub_town_15",               "Yalen"),
	("hub_town_16",               "Dhirim"),
	("hub_town_17",               "Ichamur"),
	("hub_town_18",               "Narra"),
	("hub_town_19",               "Shariz"),
	("hub_town_20",               "Durquba"),
	("hub_town_21",               "Ahmerrad"),
	("hub_town_22",               "Bariyye"),
	### TOWNS END : CASTLES BEGIN ###
	("hub_castle_1",              "Culmarr Castle"),
	("hub_castle_2",              "Malayurg Castle"),
	("hub_castle_3",              "Bulugha Castle"),
	("hub_castle_4",              "Radoghir Castle"),
	("hub_castle_5",              "Tehlrog Castle"),
	("hub_castle_6",              "Tilbaut Castle"),
	("hub_castle_7",              "Sungetche Castle"),
	("hub_castle_8",              "Jeirbe Castle"),
	("hub_castle_9",              "Jamiche Castle"),
	("hub_castle_10",             "Alburq Castle"),
	("hub_castle_11",             "Curin Castle"),
	("hub_castle_12",             "Chalbek Castle"),
	("hub_castle_13",             "Kelredan Castle"),
	("hub_castle_14",             "Maras Castle"),
	("hub_castle_15",             "Ergellon Castle"),
	("hub_castle_16",             "Almerra Castle"),
	("hub_castle_17",             "Distar Castle"),
	("hub_castle_18",             "Ismirala Castle"),
	("hub_castle_19",             "Yruma Castle"),
	("hub_castle_20",             "Derchios Castle"),
	("hub_castle_21",             "Ibdeles Castle"),
	("hub_castle_22",             "Unuzdaq Castle"),
	("hub_castle_23",             "Tevarin Castle"),
	("hub_castle_24",             "Reindi Castle"),
	("hub_castle_25",             "Ryibelet Castle"),
	("hub_castle_26",             "Senuzgda Castle"),
	("hub_castle_27",             "Rindyar Castle"),
	("hub_castle_28",             "Grunwalder Castle"),
	("hub_castle_29",             "Nelag Castle"),
	("hub_castle_30",             "Asugan Castle"),
	("hub_castle_31",             "Vyincourd Castle"),
	("hub_castle_32",             "Knudarr Castle"),
	("hub_castle_33",             "Etrosq Castle"),
	("hub_castle_34",             "Hrus Castle"),
	("hub_castle_35",             "Haringoth Castle"),
	("hub_castle_36",             "Jelbegi Castle"),
	("hub_castle_37",             "Dramug Castle"),
	("hub_castle_38",             "Tulbuk Castle"),
	("hub_castle_39",             "Slezkh Castle"),
	("hub_castle_40",             "Uhhun Castle"),
	("hub_castle_41",             "Jameyyed Castle"),
	("hub_castle_42",             "Teramma Castle"),
	("hub_castle_43",             "Sharwa Castle"),
	("hub_castle_44",             "Durrin Castle"),
	("hub_castle_45",             "Caraf Castle"),
	("hub_castle_46",             "Weyyah Castle"),
	("hub_castle_47",             "Samarra Castle"),
	("hub_castle_48",             "Bardaq Castle"),
	### CASTLES END : VILLAGES BEGIN ###
	("hub_village_1",             "Yaragar"),
	("hub_village_2",             "Burglen"),
	("hub_village_3",             "Azgad"),
	("hub_village_4",             "Nomar"),
	("hub_village_5",             "Kulum"),
	("hub_village_6",             "Emirin"),
	("hub_village_7",             "Amere"),
	("hub_village_8",             "Haen"),
	("hub_village_9",             "Buvran"),
	("hub_village_10",            "Mechin"),
	("hub_village_11",            "Dusturil"),
	("hub_village_12",            "Emer"),
	("hub_village_13",            "Nemeja"),
	("hub_village_14",            "Sumbuja"),
	("hub_village_15",            "Ryibelet"),
	("hub_village_16",            "Shapeshte"),
	("hub_village_17",            "Mazen"),
	("hub_village_18",            "Ulburban"),
	("hub_village_19",            "Hanun"),
	("hub_village_20",            "Uslum"),
	("hub_village_21",            "Bazeck"),
	("hub_village_22",            "Shulus"),
	("hub_village_23",            "Ilvia"),
	("hub_village_24",            "Ruldi"),
	("hub_village_25",            "Dashbigha"),
	("hub_village_26",            "Pagundur"),
	("hub_village_27",            "Glunmar"),
	("hub_village_28",            "Tash Kulun"),
	("hub_village_29",            "Buillin"),
	("hub_village_30",            "Ruvar"),
	("hub_village_31",            "Ambean"),
	("hub_village_32",            "Tosdhar"),
	("hub_village_33",            "Ruluns"),
	("hub_village_34",            "Ehlerdah"),
	("hub_village_35",            "Fearichen"),
	("hub_village_36",            "Jayek"),
	("hub_village_37",            "Ada Kulun"),
	("hub_village_38",            "Ibiran"),
	("hub_village_39",            "Reveran"),
	("hub_village_40",            "Saren"),
	("hub_village_41",            "Dugan"),
	("hub_village_42",            "Dirigh Aban"),
	("hub_village_43",            "Zagush"),
	("hub_village_44",            "Peshmi"),
	("hub_village_45",            "Bulugur"),
	("hub_village_46",            "Fedner"),
	("hub_village_47",            "Epeshe"),
	("hub_village_48",            "Veidar"),
	("hub_village_49",            "Tismirr"),
	("hub_village_50",            "Karindi"),
	("hub_village_51",            "Jelbegi"),
	("hub_village_52",            "Amashke"),
	("hub_village_53",            "Balanli"),
	("hub_village_54",            "Chide"),
	("hub_village_55",            "Tadsamesh"),
	("hub_village_56",            "Fenada"),
	("hub_village_57",            "Ushkuru"),
	("hub_village_58",            "Vezin"),
	("hub_village_59",            "Dumar"),
	("hub_village_60",            "Tahlberl"),
	("hub_village_61",            "Aldelen"),
	("hub_village_62",            "Rebache"),
	("hub_village_63",            "Rduna"),
	("hub_village_64",            "Serindiar"),
	("hub_village_65",            "Iyindah"),
	("hub_village_66",            "Fisdnar"),
	("hub_village_67",            "Tebandra"),
	("hub_village_68",            "Ibdeles"),
	("hub_village_69",            "Kwynn"),
	("hub_village_70",            "Dirigsene"),
	("hub_village_71",            "Tshibtin"),
	("hub_village_72",            "Elberl"),
	("hub_village_73",            "Chaeza"),
	("hub_village_74",            "Ayyike"),
	("hub_village_75",            "Bhulaban"),
	("hub_village_76",            "Kedelke"),
	("hub_village_77",            "Rizi"),
	("hub_village_78",            "Sarimish"),
	("hub_village_79",            "Istiniar"),
	("hub_village_80",            "Vayejeg"),
	("hub_village_81",            "Odasan"),
	("hub_village_82",            "Yalibe"),
	("hub_village_83",            "Gisim"),
	("hub_village_84",            "Chelez"),
	("hub_village_85",            "Ismirala"),
	("hub_village_86",            "Slezkh"),
	("hub_village_87",            "Udiniad"),
	("hub_village_88",            "Tulbuk"),
	("hub_village_89",            "Uhhun"),
	("hub_village_90",            "Jamiche"),
	("hub_village_91",            "Ayn Assuadi"),
	("hub_village_92",            "Dhibbain"),
	("hub_village_93",            "Qalyut"),
	("hub_village_94",            "Mazigh"),
	("hub_village_95",            "Tamnuh"),
	("hub_village_96",            "Habba"),
	("hub_village_97",            "Sekhtem"),
	("hub_village_98",            "Mawiti"),
	("hub_village_99",            "Fishara"),
	("hub_village_100",           "Iqbayl"),
	("hub_village_101",           "Uzgha"),
	("hub_village_102",           "Shibal Zumr"),
	("hub_village_103",           "Mijayet"),
	("hub_village_104",           "Tazjunat"),
	("hub_village_105",           "Aab"),
	("hub_village_106",           "Hawaha"),
	("hub_village_107",           "Unriya"),
	("hub_village_108",           "Mit Nun"),
	("hub_village_109",           "Tilimsal"),
	("hub_village_110",           "Rushdigh"),
	### VILLAGES END ###
	("hub_salt_mine",             "the Salt Mine"),
	
	
	("hub_excess_1",              "XXX"),
	("hub_excess_2",              "XXX"),
	("hub_excess_3",              "XXX"),
	("hub_excess_4",              "XXX"),
	("hub_excess_5",              "XXX"),
	("hub_excess_6",              "XXX"),
	("hub_excess_7",              "XXX"),
	("hub_excess_8",              "XXX"),
	("hub_excess_9",              "XXX"),
	("hub_excess_10",             "XXX"),
	("hub_excess_11",             "XXX"),
	("hub_excess_12",             "XXX"),
	("hub_excess_13",             "XXX"),
	("hub_excess_14",             "XXX"),
	("hub_excess_15",             "XXX"),
	("hub_excess_16",             "XXX"),
	("hub_excess_17",             "XXX"),
	("hub_excess_18",             "XXX"),
	("hub_excess_19",             "XXX"),
	("hub_excess_20",             "XXX"),
	("hub_excess_21",             "XXX"),
	("hub_excess_22",             "XXX"),
	("hub_excess_23",             "XXX"),
	("hub_excess_24",             "XXX"),
	("hub_excess_25",             "XXX"),
	("hub_excess_26",             "XXX"),
	("hub_excess_27",             "XXX"),
	("hub_excess_28",             "XXX"),
	("hub_excess_29",             "XXX"),
	("hub_excess_30",             "XXX"),
	("hub_excess_31",             "XXX"),
	("hub_excess_32",             "XXX"),
	("hub_excess_33",             "XXX"),
	("hub_excess_34",             "XXX"),
	("hub_excess_35",             "XXX"),
	("hub_excess_36",             "XXX"),
	("hub_excess_37",             "XXX"),
	
	### QUESTUTIL_STRINGS
	# Reasons to award a noble.
	("noble_joins_due_to_tournament",               "Inspired by your win in the recent tournament, "),
	("noble_joins_due_to_rtr",                      "Convinced that you have the right idealogy to lead, "),
	("noble_joins_due_to_siege",                    "Having witnessed the fall of {s21}, "),
	
	("ui_crouch",                 "Crouch"),
	("ui_order_7",                "Select Order 7"),
	("ui_order_8",                "Select Order 8"),
]

from util_common import *

def modmerge_strings(orig_strings):
    # add remaining strings
    from util_common import add_objects
    num_appended, num_replaced, num_ignored = add_objects(orig_strings, strings)
    #print num_appended, num_replaced, num_ignored
	
	
# Used by modmerger framework version >= 200 to merge stuff
# This function will be looked for and called by modmerger if this mod is active
# Do not rename the function, though you can insert your own merging calls where indicated
def modmerge(var_set):
    try:
        var_name_1 = "strings"
        orig_strings = var_set[var_name_1]
        modmerge_strings(orig_strings)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)
