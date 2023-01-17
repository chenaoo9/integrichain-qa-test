from selenium import webdriver


#Scenario 1 function

def check_first_n_search_results(n, word):
	results = driver.find_elements('css selector','.g')
	del results[1:5] 	#I deleted the results of the related questions 


	for index, result in enumerate(results[:n]):
		if word not in result.text.lower():
			print(f'the word {word} is not in the result {index + 1}')
			return False

	print(f'the word {word} was found in each result')
	return True

#Scenario 2 function

def check_first_result_title(word):
	result = driver.find_element('xpath',"//div[@class='MjjYud']")
	result.click()
	title = driver.title.lower()
	if word not in title:
		print(f'the word {word} was not found in the title')
		return False

	print(f'the word {word} was found in the title')
	return True


driver = webdriver.Chrome()
driver.get("https://www.google.com/")

search_box = driver.find_element('name','q')
search_box.send_keys('test automation')
search_box.submit()

print(check_first_n_search_results(3,"automation"))

print(check_first_result_title("automation"))












