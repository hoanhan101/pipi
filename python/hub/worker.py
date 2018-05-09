"""
    worker.py - Sample code using Publisher
    Author: Hoanh An (hoanhan@bennington.edu)
    Date: 05/09.2018
"""

from publisher import Publisher

if __name__ == '__main__':
    sample_data = {
        'key': 'value'
    }

    worker = Publisher()
    worker.get('test')
    worker.publish('test', sample_data)
