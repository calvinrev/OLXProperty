import requests, logging
from bs4 import BeautifulSoup as bs

def getKecList():
    try:
        print("Please wait, updating kecamatan list...")
        params = {
        'access_key': 'e214796796f18bb26937c5e50082440b',
        'url': 'https://www.olx.co.id/locations.xml'
        }
        api_result = requests.get('http://api.scrapestack.com/scrape', params)
        website_content = api_result.content
        soup = bs(website_content)

        all_loc_tag = soup.find_all("loc")
        
        prov  = list()
        kabkot= list()
        kec   = list()

        if all_loc_tag:
            print('loc:',len(all_loc_tag))
            for i in all_loc_tag:
                i = i.text
                if '_g2' in i:
                    prov.append(i)
                elif '_g4' in i:
                    kabkot.append(i)
                elif '_g5' in i:
                    kec.append(i)
            logging.info('-Jumlah Provinsi:',len(prov))
            logging.info('-Jumlah Kabupaten/Kota:',len(kabkot))
            logging.info('-Jumlah Kecamatan:',len(kec))

            #save as file
            with open('data/kecList.txt', 'w') as f:
                for item in kec:
                    f.write("%s\n" % item)

            #kecamatan list
            kecList = [i.split('_g')[-1] for i in kec]
            return kecList

        else:
            logging.warning('Kecamatan Data is Empty!')
            logging.warning('Using the latest data...')

            #read text file into kecamatan list
            kecFile = open('data/kecList.txt', 'r')
            kecFile = kecFile.read().split("\n")
            kecList = [i.split('_g')[-1] for i in kecFile]
            return kecList
    
    except Exception as e:
        logging.critical(e, exc_info=True)
        return None