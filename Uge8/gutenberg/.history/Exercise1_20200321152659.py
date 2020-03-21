# Vi henter info om alle bøgerne fra side1
# title, author, downloads

import selenium_gutenberg
res = selenium_gutenberg.get_info('sherlock holmes conan')
selenium_gutenberg.save_to_file('\n\n'.join(res))
