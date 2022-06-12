

def test_url():

    url = "https://www.flashscore.com/"
    response = requests.get(url)
    print(response.status_code)
    print(response.headers.get('Server'))
    assert response.status_code ==200


if __name__== "__main__":
    main()
