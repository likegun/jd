# -*- coding: UTF-8 -*-
import scrapy
import re

from jd.items import CommodityItem


class SearchSpider(scrapy.Spider):
    name = "search"
    allowed_domains = ["jd.com"]
    start_urls = []

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
    
    def getPageCount(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
        pageCount = re.search(r'page_count:\"(\d+)\"', response.body).group(1)
        print('---------')
        print(pageCount)
        
    # 搜索第一页
    def start_requests(self):
        return [
            scrapy.Request(
                url='https://search.jd.com/s_new.php?keyword=%E8%A3%A4%E5%AD%90&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&suggest=1.his.0.0&page=1&s=1&click=0', 
                callback=self.getPageCount,
                headers={
                    ':authority': 'search.jd.com',
                    ':method': 'GET',
                    ':path': '/s_new.php?keyword=%E8%A3%A4%E5%AD%90&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E8%A3%A4%E5%AD%90&page=3&s=54&click=0',
                    ':scheme': 'https',
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
                    'cookie': 'pinId=6PJ-5uUfprXg53blt0xYRw; qrsc=3; 3AB9D23F7A4B3C9B=3UHUCDP2YR7K7FJB5FXNBPKJASZJXXWXUZI4DZRS7ZKLXUDOAMPXCRMAPAHBTXIL2V2CMQMX7YNA5MIOMMIFH2HUFU; __jdu=14924861968681398529681; xtest=8443.cf6b6759; user-key=cd4d001b-2928-46fd-909f-5289ca5d7d52; pin=15958001874_p; unick=jd159580jra; _tp=NEKlzxIwinlS770hstC9KQ%3D%3D; _pst=15958001874_p; ipLoc-djd=15-1213-2963-49963.307139147; ipLocation=%u6d59%u6c5f; flow_outsite_ad=2_www.baidu.com__0_0_1831689_1833174_20180426175820; cn=19; shshshfp=0d291d62f07f5211598ac81cbdad93f5; shshshfpa=e60ed43a-9770-da52-8711-5dd782427c45-1525251757; shshshfpb=0b6bf15ea4265f40fa15b5798fb454be7bf0eb2553d93eb985ae97ead0; OUTFOX_SEARCH_USER_ID_NCOO=1497467355.8997877; unpl=V2_ZzNtbUtSFhAlXxJTeBsLUWIFGw4RBUpGcwFBUn0RCVZjCkcIclRCFXwUR1BnGFUUZwQZWUZcQR1FCHZXfBpaAmEBFl5yBBNNIEwEACtaDlwJBBpUQ1NLEXUITl1LKV8FVwMTbUJSSxZwAUFUcx5VAm4DEFVLU0AdcgFGZEsebDVXBBFUQ1NHJXQ4R2Q5TQAMYwoVW0AaQxB9C0NdfBlUAm4EG11AX0oRdgBBXXspXTVk; CCC_SE=ADC_VL1AoI9kEcl41%2bxSfHNtl36bkk%2b3fL8zBlA%2bxqo3vAkLL50S4xKNaBUz7wqCuRLL%2fM4EuLF5o%2bJzmpJOKhz0qAOiMoTYkNr2G39KypDouDA2IcoBNcrfE4p%2bpM%2f76pwBgCDU4C%2fsmgBRzGw9oIk%2bjV%2fb7ntsV7Y%2fV9nUQq5B%2f93aZ4JwiXV0TrLQP6WfWPhQ%2bSmQUjvJFQOR7NDWLHJMzsSl52bz8ZuFSTBLu2UOiSQeu6BPLrzuT3o6bHDSJiFLvpEmcSuKX%2b0ggFCmy6cnHIvTKK5JaPDnPkKu%2fZ7cBPIyFjcoVuzgLcsllR6Zeszbzjb%2fFWc9WFRjpmwIH7BzbSZUJg7urBPn6BMC8a7YDfhYTOxLDDcZ5%2fnGuteUnKsgF%2fxcZHykdcqRXJk%2bcNx4yVIRbe%2fKlwoVuRHRqej2vo4A5xQb6ZIJl0cf8AOHNLY474P0T7fXqeHKJSuBiPQOlodfx7qKGgyT0GHdoSvcF6OBmbjeF6LT6rDw6efdJiRU5rLFppv2veJd4eUeHEjgm%2fSpl9xkLAp7lsj5gci80hCSgxtYZdt%2f%2fubqTedhM7Cl; __jdc=122270672; PCSYCityID=1213; _jrda=6; wlfstk_smdl=i9bvvs88pkjh9jchl99ia3t5ujqblyw4; TrackID=1pYHyBOIn8e0RlpPYryhl0hf4zwjZsJ4zXjVGrI8ZPKq4D4NpAM8OB1gQc-E-kon-AEV2msux8GTpjfZ3LbIeryjCJGbHn8MwCWdrA5Tx-PFSC6YckkTAKIVK474o3vSx; ceshi3.com=103; __jdv=122270672|baidu|-|organic|not set|1525770453695; rkv=V0000; __jda=122270672.14924861968681398529681.1492486197.1525837785.1525844498.34; thor=B0B34396C3E68BFF615EC2EF68D633DFB1200F57042A772BC95CD08B4C058EA0AF7A3C7D1FC69F09D6A477470C21843375F5BBB0CC9B5D0BF3DF684918B4282F95467589A35154382622B5E575469699EA8218FC19277A845EF3E4A5E7F10BE76C149BFB7529D0502A341B76D549468F1084DEDF5A78044E1C3A488D1DFADA7A173DB84E836C3A166C11843A452825DC; shshshsID=b27bf72aadbf5f03f05b03ed6cdd4f5f_1_1525844499891; __jdb=122270672.2.14924861968681398529681|34.1525844498',
                    'referer': 'https://search.jd.com/Search?keyword=%E8%A3%A4%E5%AD%90&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E8%A3%A4%E5%AD%90&page=3&s=54&click=0',
                    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
                    'x-requested-with': 'XMLHttpRequest'
                }
            )
        ]