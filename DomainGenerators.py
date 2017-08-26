import configuration

from string import ascii_lowercase
from itertools import product


class DomainGenerator(object):

    def get_domains(self, file_name):

        with open(file_name, 'r') as file:

            return [line.replace('\n', '') + configuration.tld for line in file]

    def generate_domains(self, number_of_letters):

        return [''.join(x) + configuration.tld for x in product(ascii_lowercase, repeat=number_of_letters)]