from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

url = "https://www.tripadvisor.com.br/"

initiation_time = datetime.utcnow()
finalization_time = datetime.utcnow()

print(f"Robô INICIADO em {initiation_time}")

option = Options()
option.headless = True
driver = webdriver.Firefox()

time.sleep(1)

driver.get(url)

time.sleep(5)
driver.find_element_by_id("onetrust-accept-btn-handler").click()
time.sleep(1)

driver.find_element_by_xpath("//div[@class='dqRmR dcDXR dJjeH']//div//div//div//form//input[@class='fhEMT _G B- z _J Cj R0']").click()

driver.find_element_by_xpath("//div[@class='dqRmR dcDXR dJjeH']//div//div//div//form//input[@class='fhEMT _G B- z _J Cj R0']").send_keys("Congresso Nacional")
time.sleep(2)

driver.find_element_by_xpath("//form[@class='bmTdH o']//div//a//div//div[@class='WlYyy cPsXC dTqpp']").click()
time.sleep(2)

avaliacao = driver.find_element_by_xpath("//div[@class='fbjOn']//div//span//div//div//div[@class='WlYyy cPsXC fksET cMKSg']").text

num_avaliacao = driver.find_element_by_xpath("//div[@class='TFQoM e']//span//div//div//div//span[@class='WlYyy diXIH bGusc dDKKM']").text

print('## Resultado da coleta de dados ##')
print(f"Avaliação do local: {avaliacao} de {num_avaliacao}")

print(f"Robô FINALIZADO com SUCESSO em {finalization_time}")


driver.quit()

