import unittest

from selenium import webdriver


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
        self.fail('Finish the test!')

        # Ela é convidada a inserri um item de tarefa imediatamente 

        # Ela digita "Buy peacock feathers" (Comprar penas de pavão) em uma caixa
        # de texto (o hoby de Gabriel é fazer iscas para pescas com fly)

        # Quando ela tecla enter, a página é atualizada, e agora a página lista
        # "1: Buy peacock feather" como um item em uma lista de tarefas

        # Ainda continua havendo uma caixa de texto convidando-a a acrecentar outro
        # item. Ela insere "Use peacock feathers to make a fly" (Usar penas de pavão
        # para fazer um fly - Edith é bem metódica)

        # A página é atualizada novamente e agora mostras os dois itens em sua lista

        # Edith se pergunta se o site lembrará de sua lista. Então ela nota
        # que o site gerou uma URL única para ela -- há um pequeno texto
        # explicativo para isso

        # Ela acessa essa URL - sua lista de tarefas continua lá

        # Satisfeita ela volta a dormir


if __name__ == '__main__':
    unittest.main()
