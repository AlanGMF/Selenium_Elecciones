from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Configura las opciones del navegador para abrir en pantalla completa
chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--headless") # Set the Chrome webdriver to run in headless mode for scalability
# chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome()
# driver = webdriver.Firefox()

# driver.get("https://resultados.gob.ar/elecciones/1/73994/1/-1/-1/C%C3%B3rdoba/Capital/00001/ESC--NACIONAL-DE-MONSERRAT/0400100009X")
driver.get("https://resultados.gob.ar/elecciones/1/73994/1/-1/-1/")

try:
    # Espera a que un elemento con el ID "element_id" esté presente en la página
    elemento = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="flex flex-col xl:flex-row"]//div[@class="flex-1 lg:max-h-[900px] lg:max-w-[1000px]"]//ul'))
    )    


    # Obtener todos los elementos "li" dentro de "elemento"
    li_elementos = elemento.find_elements(By.TAG_NAME, 'li')

    # Iterar a través de los elementos "li"
    for li in li_elementos:

        # Encontrar el elemento "p" dentro de cada elemento "li"
        partido = li.find_element(By.TAG_NAME, 'p')
        votos = li.find_element(By.TAG_NAME, 'span')

        # Obtener el texto dentro del elemento "p"
        texto_p = votos.text
        texto_p = partido.text
        # Imprimir o procesar el texto según sea necesario
        print(votos.text)
        print(partido.text)

    driver.quit()

except Exception:
    # En caso de que expire el tiempo de espera
    print("Elemento no encontrado en la página.")

finally:
     # Obtiene la URL actual
    url_actual = driver.current_url

    # Imprime la URL o realiza cualquier otra operación que desees
    print("URL actual:", url_actual)
    # Cierra el navegador

    driver.quit()