import requests
import sys


def news(sort,inc,lang,pagee,howmany,wantcontent):
    url = f"https://newsapi.org/v2/everything"
    param = {
        "apiKey": "your api key hereee",
        "sortBy": sort,
        "q": inc,
        "language": lang,
        "page":pagee,
     }
    try:
        res=requests.get(url,params=param)
        data=res.json();
        articles=data.get("articles",[])
        print(f"Total results are {data.get('totalResults')} out of which showing {howmany}")

        for i,article in enumerate(articles[:howmany], 1):
            print(f"{i}.{article.get('title')}")
            print(article.get("description"))
            if(wantcontent==True):
                print(f"Full content below \n {article.get('content')}")
            print(article.get('publishedAt'))
            print(article.get('url'))
            print(f"Source={article.get('source',{}).get('name')}")


    except requests.exceptions.RequestException as e:
        print(f"An internet connection error occurred: {e}")



search=input("What to search \n")

filters=input("Do you want to turn on filters?\nDefault values with no detailed content will be provided if anything other then yes is provided")
if(filters.lower()=="on" or filters.lower()=="yes" or filters.lower()=="filterson"):



            sort=int(input("How to sort \nPress 1 to sort by relevence \nPress 2 to sort by popularity \nPress 3 to sort by date\nNote default is relevence\n"))
            sortt="";
            if(sort==1):
                sortt="relevancy"
            elif(sort==2):
                sortt="popularity"
            elif(sort==3):
                sortt="publishedAt"
            else:
                sortt="relevency"

            language=input("Enter 2 digits iso code of language \n")
            page=int(input("What page results you want?"))
            if(page==0 or page <=0):
                print("Pages cant be 0 or negative")
                sys.exit();
            totalres=int(input("How many results u want?"))
            if(totalres==0 or totalres <=0):
                    print("Number of results cant be 0 or negative")
                    sys.exit();
            a=False;
            content=input("should content be on?")
            if(content.lower() in ["on","yes"]):
                a=True;
            elif(content.lower() in ["off","no"]):
                a=False;
            else:
                print("Invalid choice.... \n Shutting down...")
                sys.exit()
            


            news(sortt,search,language,page,totalres,a)
else:





 news("relevency",search,"en",1,7,False)
