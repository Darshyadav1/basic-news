import streamlit as st
import requests
import time

#sort,news,en,page,pageee,want

st.set_page_config(
    page_title="Article fetcher",  # Changes the text on the browser tab
    page_icon="⚡",                        # Changes the tiny favicon tab icon (can use emojis!)
    layout="centered"                      # Can be "centered" or "wide"
)



with st.spinner("Refreshing components..."):
    time.sleep(1)



    st.header("Your latest news updated here")
    news = st.text_input("Search",placeholder="Enter your search queue here", icon=":material/search:")

    userf = st.checkbox("Enable advance filters")


    sortt=""
    sort=""
    pageee=5
    page=1
    if userf:
        with st.spinner("Refreshing components..."):
            time.sleep(0.6)
            sortt= st.radio("Sort by" , [ "Popularity","Releviency","Date"])
            
            if(sortt=="Popularity"):
                sort="popularity"
            elif(sortt=="Releviency"):
                sort="relevancy"
            elif(sortt=="Date"):
                sort="publishedAt"
            page=st.number_input("What page to fetch", min_value=1,max_value=100 )
            pageee=st.number_input("How many results to display", min_value=5,max_value=50 )



    want=st.checkbox("Want detailed content?")

    fetch=st.button("Fetch latest news", type="primary",help="Fetch latest news", width=400)
    if(fetch):
        if(news==""):
            st.warning("Please enter something in the search bar")
        else:
            url=f"https://newsapi.org/v2/everything"
            param = {
                "apiKey": "732d06ab20d849238f21d723330cc938",
                "sortBy": sort,
                "q": news,
                "language": "en",
                "pageSize":pageee,
                "page": page,
            }
            with st.spinner("Featching your news"):
                try:
                    res=requests.get(url,params=param)
                    data=res.json()
                    ar=data.get("articles",[])
                    st.success(f"Total results are {data.get('totalResults',0)} out of which showing {len(ar)}")
                    
                    for i,article in enumerate(ar[:pageee + 1],1):
                        st.divider()
                        st.title(f"{i}.{article.get('title')}")
                        st.subheader(article.get('description'))
                        st.divider(width=200)
                        if want:
                            st.write(article.get('content'))
                        else:
                            st.warning("Full contex off")
                        st.write(f"Published at {article.get('publishedAt')} on {article.get('source',{}).get('name','unknown')}")
                        st.markdown(f"[Read oiginal article]({article.get('url')})")
                        st.divider(width=200)
                        st.divider()
                except requests.exceptions.RequestException as e:
                    st.error(f"Network Connection Failed: {e}")








