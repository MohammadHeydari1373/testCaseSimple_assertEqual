import unittest
import cap 
class TestCap(unittest.TestCase):
	def test_one_word(self):
		text = "python"
		result = cap.cap_test(text)
		self.assertEqual(result , 'python'.capitalize())
	def test_multiple_word(self) :
		text = "monty python" 
		result = cap.cap_test(text)
		self.assertEqual(result,"monty python".capitalize())
if __name__ == '__main__':
	unittest.main()

		