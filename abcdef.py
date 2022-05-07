try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# to search
# jobs = ["actor", "anactor", "baker", "butcher", "carpenter", "cook", "farmer", "doctor", "engineer", "farmer", "fireworker", "fisherman", "gardener", "goldsmith", "hairdresser", "journalist", "lawyer", "mason", "mechanic", "nurse", "painter", "plumber", "postman", "secretary", "shoe-shineboy", "singer", "tailor", "teacher"]

# for item in range(0, len(jobs)):

query = "gardening huntington park"
# query = jobs[item]+" irvine"
# in order to loop in jobs
for j in search(query, tld="fr", num=10, stop=200, pause=3):
    print(j)
    if j[4] != 's':

        with open("result.txt", "a") as myfile:
            myfile.write(j+"\n")
            # write the result in result.txt file
