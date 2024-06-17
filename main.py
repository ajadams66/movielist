import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
from datetime import date

today = date.today()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.boxofficemojo.com/')
time.sleep(3)

weekly_movies = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[4]/div/a[3]')
weekly_movies.click()
time.sleep(5)
# Movie 1
movie1 = driver.find_element(By.XPATH, '//*[@id="table"]/div/table[2]/tbody/tr[2]/td[7]/a')
movie1_name = movie1.text
movie1_release = driver.find_element(By.XPATH,
                                     value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[2]/td[6]')
movie1_release = movie1_release.text
movie1_gross = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[2]/td[4]')
movie1_gross = movie1_gross.text
movie1_week = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[2]/td[11]/a')
movie1_week = movie1_week.text
movie1_link = driver.find_element(By.XPATH,
                                  value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[2]/td[7]/a')
movie1_link = movie1_link.get_attribute('href')
# Movie_2
movie2 = driver.find_element(By.XPATH, value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[3]/td[7]/a')
movie2_name = movie2.text
movie2_release = driver.find_element(By.XPATH,
                                     value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[3]/td[6]')
movie2_release = movie2_release.text
movie2_gross = driver.find_element(By.XPATH,
                                   value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[3]/td[4]')
movie2_gross = movie2_gross.text
movie2_week = driver.find_element(By.XPATH,
                                  value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[3]/td[11]/a')
movie2_week = movie2_week.text
movie2_link = driver.find_element(By.XPATH,
                                  value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[3]/td[7]/a')
movie2_link = movie2_link.get_attribute('href')
# Movie_3
movie3 = driver.find_element(By.XPATH, value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[4]/td[7]/a')
movie3_name = movie3.text
movie3_release = driver.find_element(By.XPATH,
                                     value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[4]/td[6]')
movie3_release = movie3_release.text
movie3_gross = driver.find_element(By.XPATH,
                                   value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[4]/td[4]')
movie3_gross = movie3_gross.text
movie3_week = driver.find_element(By.XPATH,
                                  value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[4]/td[11]/a')
movie3_week = movie3_week.text
movie3_link = driver.find_element(By.XPATH,
                                  value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[4]/td[7]/a')
movie3_link = movie3_link.get_attribute('href')
# Movie_4
movie4 = driver.find_element(By.XPATH, value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[5]/td[7]/a')
movie4_name = movie4.text
movie4_release = driver.find_element(By.XPATH,
                                     value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[5]/td[6]')
movie4_release = movie4_release.text
movie4_gross = driver.find_element(By.XPATH,
                                   value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[5]/td[4]')
movie4_gross = movie4_gross.text
movie4_week = driver.find_element(By.XPATH,
                                  value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[5]/td[11]/a')
movie4_week = movie4_week.text
movie4_link = driver.find_element(By.XPATH,
                                  value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[5]/td[7]/a')
movie4_link = movie4_link.get_attribute('href')
# Movie_5
movie5 = driver.find_element(By.XPATH, value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[6]/td[7]/a')
movie5_name = movie5.text
movie5_release = driver.find_element(By.XPATH,
                                     value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[6]/td[6]')
movie5_release = movie5_release.text
movie5_gross = driver.find_element(By.XPATH,
                                   value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[6]/td[4]')
movie5_gross = movie5_gross.text
movie5_week = driver.find_element(By.XPATH,
                                  value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[6]/td[11]/a')
movie5_week = movie5_week.text
movie5_link = driver.find_element(By.XPATH,
                                  value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[6]/td[7]/a')
movie5_link = movie5_link.get_attribute('href')
# Movie_6
movie6 = driver.find_element(By.XPATH, value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[7]/td[7]/a')
movie6_name = movie6.text
movie6_release = driver.find_element(By.XPATH,
                                     value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[7]/td[6]')
movie6_release = movie6_release.text
movie6_gross = driver.find_element(By.XPATH,
                                   value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[7]/td[4]')
movie6_gross = movie6_gross.text
movie6_week = driver.find_element(By.XPATH,
                                  value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[7]/td[11]/a')
movie6_week = movie6_week.text
movie6_link = driver.find_element(By.XPATH,
                                  value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[7]/td[7]/a')
movie6_link = movie6_link.get_attribute('href')
# Movie_7
movie7 = driver.find_element(By.XPATH, value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[8]/td[7]/a')
movie7_name = movie7.text
movie7_release = driver.find_element(By.XPATH,
                                     value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[8]/td[6]')
movie7_release = movie7_release.text
movie7_gross = driver.find_element(By.XPATH,
                                   value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[8]/td[4]')
movie7_gross = movie7_gross.text
movie7_week = driver.find_element(By.XPATH,
                                  value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[8]/td[11]/a')
movie7_week = movie7_week.text
movie7_link = driver.find_element(By.XPATH,
                                  value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[8]/td[7]/a')
movie7_link = movie7_link.get_attribute('href')
# Movie_8
movie8 = driver.find_element(By.XPATH, value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[9]/td[7]/a')
movie8_name = movie8.text
movie8_release = driver.find_element(By.XPATH,
                                     value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[9]/td[6]')
movie8_release = movie8_release.text
movie8_gross = driver.find_element(By.XPATH,
                                   value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[9]/td[4]')
movie8_gross = movie8_gross.text
movie8_week = driver.find_element(By.XPATH,
                                  value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[9]/td[11]/a')
movie8_week = movie8_week.text
movie8_link = driver.find_element(By.XPATH,
                                  value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[9]/td[7]/a')
movie8_link = movie8_link.get_attribute('href')
# Movie_9
movie9 = driver.find_element(By.XPATH, value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[10]/td[7]/a')
movie9_name = movie9.text
movie9_release = driver.find_element(By.XPATH,
                                     value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[10]/td[6]')
movie9_release = movie9_release.text
movie9_gross = driver.find_element(By.XPATH,
                                   value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[10]/td[4]')
movie9_gross = movie9_gross.text
movie9_week = driver.find_element(By.XPATH,
                                  value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[10]/td[11]/a')
movie9_week = movie9_week.text
movie9_link = driver.find_element(By.XPATH,
                                  value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[10]/td[7]/a')
movie9_link = movie9_link.get_attribute('href')
# Movie_10
movie10 = driver.find_element(By.XPATH, value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[11]/td[7]/a')
movie10_name = movie10.text
movie10_release = driver.find_element(By.XPATH,
                                      value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[11]/td[6]')
movie10_release = movie10_release.text
movie10_gross = driver.find_element(By.XPATH,
                                    value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[11]/td[4]')
movie10_gross = movie10_gross.text
movie10_week = driver.find_element(By.XPATH,
                                   value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[11]/td[11]/a')
movie10_week = movie10_week.text
movie10_link = driver.find_element(By.XPATH,
                                   value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[11]/td[7]/a')
movie10_link = movie10_link.get_attribute('href')
# Movie_11
movie11 = driver.find_element(By.XPATH, value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[12]/td[7]/a')
movie11_name = movie11.text
movie11_release = driver.find_element(By.XPATH,
                                      value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[12]/td[6]')
movie11_release = movie11_release.text
movie11_gross = driver.find_element(By.XPATH,
                                    value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[12]/td[4]')
movie11_gross = movie11_gross.text
movie11_week = driver.find_element(By.XPATH,
                                   value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[12]/td[11]/a')
movie11_week = movie11_week.text
movie11_link = driver.find_element(By.XPATH,
                                   value='/html/body/div[1]/main/div/div/div[3]/div/table[2]/tbody/tr[12]/td[7]/a')
movie11_link = movie11_link.get_attribute('href')
Movie = {
    'Movie': [movie1_name, movie2_name, movie3_name, movie4_name, movie5_name,
              movie6_name, movie7_name, movie8_name, movie9_name, movie10_name, movie11_name],
    'release': [movie1_release, movie2_release, movie3_release, movie4_release, movie5_release,
                movie6_release, movie7_release, movie8_release, movie9_release, movie10_release, movie11_release],
    'gross': [movie1_gross, movie2_gross, movie3_gross, movie4_gross, movie5_gross,
              movie6_gross, movie7_gross, movie8_gross, movie9_gross, movie10_gross, movie11_gross],
    'week': [movie1_week, movie2_week, movie3_week, movie4_week, movie5_week,
             movie6_week, movie7_week, movie8_week, movie9_week, movie10_week, movie11_week],
    'Link': [movie1_link, movie2_link, movie3_link, movie4_link, movie5_link, movie6_link, movie7_link, movie8_link,
             movie9_link, movie10_link, movie11_link]
}
movie_list = pd.DataFrame.from_dict(Movie)
movie_list.to_csv(f'MovieList-{today}.csv', index=False)
