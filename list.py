import glob
from pprint import pprint
import oyaml as yaml
import os

files = glob.glob("fa18*/README.yml")

#pprint (files)
readmes = {}
for readme in files:
    with open(readme, 'r') as stream:
        filename = readme.replace("/README.yml","") # use dir name or so
        try:
            d = yaml.load(stream)
            readmes[filename] = d
        except yaml.YAMLError as exc:
            print(exc)


#pprint (readmes)

# print(yaml.dump(readmes, default_flow_style=False))


counter = 1

def print_community(community):
    global counter
    print ("| n | semester | hid | lastname | firstname | community | t1 | t2 | t3 | t4 | t5 | t6 | paper | project |")
    print ("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---| --- | --- |")
    for hid in readmes:
        entry = {
            "semester": "ERROR",
            "readme": "ERROR",
            "hid": "ERROR",
            "firstname": "ERROR",
            "lastname": "ERROR",
            "community": "ERROR",
            "t1": "ERROR",
            "t2": "ERROR",
            "t3": "ERROR",
            "t4": "ERROR",
            "t5": "N/A",
            "t6": "N/A",
            "paper": "ERROR",
            "project": "ERROR",
            "projectkey": "project",
            "paperkey": "paper",                                
            }
        try:
            s = readmes[hid]
            entry["readme"] = "[{hid}](https://github.com/cloudmesh-community/{hid}/blob/master/README.yml)".format(hid=hid)
            entry["hid"] = hid
            entry["lastname"] = s["owner"]["lastname"]
            entry["firstname"] = s["owner"]["firstname"]
            entry["community"] = s["owner"]["community"]
            if "semester" in s["owner"]:
                entry["semester"] = s["owner"]["semester"]

            #print (entry["community"])
            #if entry["community"] not hid:
            #    break;
            
            if "516" in entry["community"]:
                for t in ["t1", "t2", "t3", "t4", "t5", "t6"]:
                     entry[t] = "N/A"
            else:
                t = ""
                c = -1
                for t in ["t1", "t2", "t3", "t4", "t5", "t6"]:
                    c = c + 1
                    try:
                        url = s["technologies"][c]["url"]
                        entry[t] = "[{t}]({url})".format(t=t,url=url)
                    except Exception as e:
                        pass

            # paper
            if "paper" in s:
              try:
                  
                  title = s["paper"][0]["title"]
                  url   = s["paper"][0]["url"]
                  if "keyword" in s["paper"][0]:
                      entry["paperkey"] = s["paper"][0]["keyword"]
                      
                  if "group" in ["paper"][0]:
                      if hid in url:
                          entry["paper"] = "[paper]({url})".format(**entry,url=url)
                      else:
                          entry["paper"] = "see [{paperkey}]({url})".format(**entry,url=url)
                  entry["paper"] = "[{paperkey}]({url})".format(**entry,url=url)
              except:
                  entry["paper"] = "TBD"

                          # paper
            if "project" in s:
              try:
                  title = s["project"][0]["title"]
                  url   = s["project"][0]["url"]
                  if "keyword" in s["project"][0]:
                      entry["projectkey"] = s["project"][0]["keyword"]
                      

                  if "group" in ["project"][0]:
                      if hid in url:
                          entry["project"] = "[{projectkey}]({url})".format(**entry, url=url)
                      else:
                          entry["project"] = "see [{projectkey}]({url})".format(**entry, url=url)
                  entry["project"] = "[{projectkey}]({url})".format(**entry,url=url)
              except:
                  entry["project"] = "TBD"


        except:
            pass
        entry["counter"] = counter
        counter = counter + 1

        print ("| {counter} | {semester} | {readme} | {lastname} | {firstname} | {community} | {t1} | {t2} | {t3} | {t4} | {t5} | {t6} | {paper} | {project} |".format(**entry))

print_community("523")
