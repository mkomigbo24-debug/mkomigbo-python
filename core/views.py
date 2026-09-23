from django.shortcuts import render

def home(request):
    # 20 subjects list - from PHP MySQL -> Python
    subjects = [
        {"slug": "history", "name": "History", "pages": 6, "desc": "Timelines, migrations, kingdoms"},
        {"slug": "culture", "name": "Culture", "pages": 5, "desc": "Arts, customs, festivals"},
        {"slug": "language1", "name": "Language 1", "pages": 5, "desc": "Origins, dialects, scripts"},
        {"slug": "lang2", "name": "Language 2", "pages": 5, "desc": "Grammar, usage - SAFE"},
        {"slug": "religion", "name": "Religion", "pages": 15, "desc": "Thesis level"},
        {"slug": "esoterism", "name": "Esoterism", "pages": 7, "desc": "Western, Eastern, African"},
        {"slug": "tradition", "name": "Tradition", "pages": 5, "desc": "Igbo institutions"},
        {"slug": "biafra", "name": "Biafra", "pages": 5, "desc": "War, causes, famine"},
        {"slug": "slavery", "name": "Slavery", "pages": 5, "desc": "Atlantic trade, osu"},
        {"slug": "nigeria", "name": "Nigeria", "pages": 5, "desc": "Politics, oil"},
        {"slug": "africa", "name": "Africa", "pages": 5, "desc": "Pre-colonial"},
        {"slug": "pogrom", "name": "Pogrom", "pages": 5, "desc": "1966 massacres"},
        {"slug": "uk", "name": "UK", "pages": 5, "desc": "Diaspora in Britain"},
        {"slug": "struggles", "name": "Struggles", "pages": 5, "desc": "Five centuries"},
        {"slug": "resistance", "name": "Resistance", "pages": 5, "desc": "IPOB"},
        {"slug": "europe", "name": "Europe", "pages": 5, "desc": "African diaspora"},
        {"slug": "arabs", "name": "Arabs", "pages": 5, "desc": "Arab-African"},
        {"slug": "about", "name": "About", "pages": 5, "desc": "What Mkomigbo is"},
        {"slug": "people", "name": "People", "pages": 5, "desc": "Equiano to Adichie"},
        {"slug": "persons", "name": "Persons", "pages": 5, "desc": "Biographical"},
    ]
    return render(request, 'core/home.html', {'subjects': subjects})