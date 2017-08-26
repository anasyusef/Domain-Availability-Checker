from CheckDomains import CheckDomain
from DomainGenerators import DomainGenerator

import configuration
import os
import logging
import extras

if __name__ == '__main__':

    # Logging configuration

    logger = logging.getLogger(__name__)

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(levelname)s: %(asctime)s - File name: {} | TLD: {} - %(message)s'
                                  .format(configuration.filename if configuration.domain_get_method ==
                                          'file' else configuration.domain_get_method,
                                          configuration.tld),
                                  datefmt="%H:%M:%S")

    file_handler = logging.FileHandler(configuration.log_filename)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.info('----------------------- Program Started! -------------------')

    foo = DomainGenerator()

    check_domain = CheckDomain()

    if configuration.domain_get_method == 'generate':
        domains = foo.generate_domains(configuration.user_input_letters)
        logger.info('Domains Generated!')
    else:
        domains = foo.get_domains(configuration.filename_domains)
        logger.info('Domains retrieved from file!')

    domains_available = 0

    logger.info("Length of the list to be checked: {}".format(len(domains)))

    print('Getting information. Program Started.')

    starting_domain_len = len(domains)

    logger.info('Length of VAR domains: {}'.format(starting_domain_len))
    while len(domains) > 0:

        domains_checked = check_domain.check_domains_bulk(domains)

        if domains_checked is False:
            logger.info('TLD is not supported')
            break

        check_domain.remove_not_available(domains_checked)

        check_domain.add_domain_price(domains_checked)

        # Special case

        if len(domains_checked) == 0:
            logger.info('No domains have been found.')
            extras.remove_found_domains(domains, CheckDomain.domains_to_check)
            logger.info('Domains left: {}'.format(len(domains)))
            continue

        domains_available += len(domains_checked)
        logger.info('{}/{} Domains found are available'.format(domains_available,
                                                               starting_domain_len))

        check_domain.transfer_into_file(domains_checked)

        extras.remove_found_domains(domains, CheckDomain.domains_to_check)

        logger.info('Domains left: {}'.format(len(domains)))
        logger.info('Domains checked: {}'.format(CheckDomain.checked))

    if os.path.isfile(configuration.filename) and configuration.domain_get_method == 'file':
        print('Program Finished. Check your {} file'.format(configuration.filename))
    else:
        print('Program Finished. No domains were found.')

    logger.info('----------------------- Program Finished! -------------------')


