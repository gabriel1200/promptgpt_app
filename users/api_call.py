def send_request(api_key,urls,question,endpoint):
    api_url = "http://137.184.62.16:80"+endpoint
    #print(api_key)

    params = {
        "api_key": api_key,
        #"url1": "https://jackhenry.co/",
        #"url2": "https://jackhenry.co/pages/about",
        #"url3": "https://jackhenry.co/products/super-face-cream",

    }
    params["question"] =question
    url_count = 0
    for url in urls:
        params["url"+str(url_count+1)] = url
        url_count+=1
    #print(urls)
    #print(question)
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        message = response.json()
        return(message)
    else:
        fail_string ="Request failed with status code:" +str(response.status_code)
        return fail_string