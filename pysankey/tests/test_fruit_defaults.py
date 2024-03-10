import matplotlib.pyplot as plt
from pysankey import sankey as sky
from .test_fruit_setup import TestFruit

class TestFruitDefault(TestFruit):

    def test_fruits_default(self):
        
        plt.figure(dpi=150)
        print(dir(sky))
        sky.sankey(self.data)
        plt.savefig("fruits_default.png")
