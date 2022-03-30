from main import get_page
def test_page_response():
    test_url =  'https://www.python.org'
    test_url1 = 'http://brochure.getpython.info/'
    test_url2 = 'http://wiki.python.org/moin/'
    test_url3 = 'http://python.org/dev/peps/'
    test_url4 = 'http://planetpython.org/hh'

    response = get_page(test_url)  # get_page() returns a response object
    assert response.status_code == 200
    
    responses = get_page(test_url1)
    print("Status Code :", + responses.status_code)
    assert responses == responses.status_code
        
    assert responses.status_code == 200
    response2 = get_page(test_url2)
    assert response2.status_code == 200
    response3 = get_page(test_url3)
    assert response3.status_code == 200
    response4 = get_page(test_url4)
    assert response4.status_code == 200
    