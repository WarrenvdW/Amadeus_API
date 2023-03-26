import pandas as pd
import blackbird_soap as bs
import blackbird_prescript as bp
import datetime

now = datetime.datetime.now()
date = now.strftime('%Y-%m-%d')

oid_list = ['JNBFB3102','JNBFB3105','JNBFB3106','JNBFB3107','JNBFB3108','JNBFB3110','JNBFB3111','PRYFB3432']

def main():
    
    for oid in oid_list:

        response = bs.soap_request(oid)

        filename = f'C:\Warren\Amadeus TJQ API\XML_files\{date}_{oid}.xml'

        with open(filename,'w') as f:
            f.write(response.text)

        print(f'{oid} API request complete')


if __name__ == '__main__':
    main()

