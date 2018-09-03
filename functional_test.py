import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self):
        # Gabriel ouviu falar de uma nova aplicação online interessante para
        # lista de tarefas. Ela decife acessar sua homepage
        self.browser.get('http://localhost:8000')

        # Ela percebe que p título da página e o cabeçalho mencionam listas de
        # tarefas (to-do)
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Ela é convidada a inserri um item de tarefa imediatamente
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Ela digita "Buy peacock feathers" (Comprar penas de pavão) em uma caixa
        # de texto (o hoby de Gabriel é fazer iscas para pescas com fly)
        inputbox.send_keys('Buy peacock feathers')

        # Quando ela tecla enter, a página é atualizada, e agora a página lista
        # "1: Buy peacock feather" como um item em uma lista de tarefas
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows ),
            'New to-do item not appear in table'
        )

        # Ainda continua havendo uma caixa de texto convidando-a a acrecentar outro
        # item. Ela insere "Use peacock feathers to make a fly" (Usar penas de pavão
        # para fazer um fly - Edith é bem metódica)
        self.fail('Finish the test!')

        # A página é atualizada novamente e agora mostras os dois itens em sua lista

        # Edith se pergunta se o site lembrará de sua lista. Então ela nota
        # que o site gerou uma URL única para ela -- há um pequeno texto
        # explicativo para isso

        # Ela acessa essa URL - sua lista de tarefas continua lá

        # Satisfeita ela volta a dormir


if __name__ == '__main__':
    unittest.main()
