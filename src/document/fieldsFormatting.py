JOURNAL_ABBREV = {"trans.":"Transactions",
                  "Trans.":"Transactions",
                  "graph.":"Graphics",
                  "Graph.":"Graphics"
                  }

def formatAuthors(authors):
    newAuthor = ""
    authorList = authors.split("and")
    newAuthorList = []
    for i, a in enumerate(authorList):
        parts = a.split(",")
        if (len(parts) == 2):
            authorStr = parts[1].strip() + " " + parts[0].strip()
            newAuthor += authorStr
            if (i != len(authorList) - 1):
                newAuthor += ", "
        else:
            print("Warning : not 2 components author")
    return newAuthor

def formatJournal(journal):
    newJournal = journal
    for abrv in JOURNAL_ABBREV.keys():
        if (abrv in newJournal):
            newJournal = newJournal.replace(abrv, JOURNAL_ABBREV[abrv])
    return newJournal
