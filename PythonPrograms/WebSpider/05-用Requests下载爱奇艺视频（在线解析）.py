from multiprocessing import Pool
import requests


session = requests.session()
content = session.get("https://api.m3u8.pw/Cache/qiyi/8a9f3fac90184c220d87b60f2fb32329.m3u8?vkey=baa2B1QCVQIDUQkJBAIHAwRQAgQHAlIIUwhUAldQAw4FDVMHVQRT")
print(content.content)
# with open("x.mp4",mode="wb") as f:
#     f.write(content)

"""
https://v-6fce1738.71edge.com/videos/vts/20191010/0e/0f/06c4b75b708e79583b4526751712a9f3.ts?key=07c9cded18862366b177d04067b4f9cbb&dis_k=22bd3faa0f913ff7099b1d1b0e66a1057&dis_t=1670851243&dis_dz=CNC-BeiJing&dis_st=141&src=iqiyi.com&dis_hit=0&dis_tag=01010000&uuid=7b7370ec-63972aab-397&start=13987840&mss=1&qd_uid=1023108576&qd_k=d117275fbf0dbee1cbf8daeb7289fc1e&sd=0&qd_tm=1670851117507&qd_vip=0&cross-domain=1&pv=0.1&ssl=1&qd_sc=8f6fed51b33eb35cf3c29b520372481d&contentlength=1193984&qyid=e25f31d1e250ba7bfb0e4929232b8498&qd_p=7b7370ec&qd_tvid=589243300&bid=500&qd_index=prv&qd_src=01010031010000000000&dis_src=tpa&stauto=1&qd_vipres=2&end=15181824&cphc=arta&ori=pcw1&num=1670851281902
https://v-6fce1738.71edge.com/videos/vts/20191010/0e/0f/06c4b75b708e79583b4526751712a9f3.ts?key=07c9cded18862366b177d04067b4f9cbb&dis_k=22bd3faa0f913ff7099b1d1b0e66a1057&dis_t=1670851243&dis_dz=CNC-BeiJing&dis_st=141&src=iqiyi.com&dis_hit=0&dis_tag=01010000&uuid=7b7370ec-63972aab-397&start=15181824&mss=1&qd_uid=1023108576&qd_k=d117275fbf0dbee1cbf8daeb7289fc1e&sd=0&qd_tm=1670851117507&qd_vip=0&cross-domain=1&pv=0.1&ssl=1&qd_sc=8f6fed51b33eb35cf3c29b520372481d&contentlength=1050624&qyid=e25f31d1e250ba7bfb0e4929232b8498&qd_p=7b7370ec&qd_tvid=589243300&bid=500&qd_index=prv&qd_src=01010031010000000000&dis_src=tpa&stauto=1&qd_vipres=2&end=16232448&cphc=arta&ori=pcw1&num=1670851282287
https://v-6fce1738.71edge.com/videos/vts/20191010/0e/0f/06c4b75b708e79583b4526751712a9f3.ts?key=07c9cded18862366b177d04067b4f9cbb&dis_k=22bd3faa0f913ff7099b1d1b0e66a1057&dis_t=1670851243&dis_dz=CNC-BeiJing&dis_st=141&src=iqiyi.com&dis_hit=0&dis_tag=01010000&uuid=7b7370ec-63972aab-397&start=16232448&mss=1&qd_uid=1023108576&qd_k=d117275fbf0dbee1cbf8daeb7289fc1e&sd=0&qd_tm=1670851117507&qd_vip=0&cross-domain=1&pv=0.1&ssl=1&qd_sc=8f6fed51b33eb35cf3c29b520372481d&contentlength=688128&qyid=e25f31d1e250ba7bfb0e4929232b8498&qd_p=7b7370ec&qd_tvid=589243300&bid=500&qd_index=prv&qd_src=01010031010000000000&dis_src=tpa&stauto=1&qd_vipres=2&end=16920576&cphc=arta&ori=pcw1&num=1670851282820
https://v-6fce1738.71edge.com/videos/vts/20191010/0e/0f/06c4b75b708e79583b4526751712a9f3.ts?key=07c9cded18862366b177d04067b4f9cbb&dis_k=22bd3faa0f913ff7099b1d1b0e66a1057&dis_t=1670851243&dis_dz=CNC-BeiJing&dis_st=141&src=iqiyi.com&dis_hit=0&dis_tag=01010000&uuid=7b7370ec-63972aab-397&start=16920576&mss=1&qd_uid=1023108576&qd_k=d117275fbf0dbee1cbf8daeb7289fc1e&sd=0&qd_tm=1670851117507&qd_vip=0&cross-domain=1&pv=0.1&ssl=1&qd_sc=8f6fed51b33eb35cf3c29b520372481d&contentlength=1465344&qyid=e25f31d1e250ba7bfb0e4929232b8498&qd_p=7b7370ec&qd_tvid=589243300&bid=500&qd_index=prv&qd_src=01010031010000000000&dis_src=tpa&stauto=1&qd_vipres=2&end=18385920&cphc=arta&ori=pcw1&num=1670851300115
https://v-6fce1738.71edge.com/videos/vts/20191010/0e/0f/06c4b75b708e79583b4526751712a9f3.ts?key=07c9cded18862366b177d04067b4f9cbb&dis_k=22bd3faa0f913ff7099b1d1b0e66a1057&dis_t=1670851243&dis_dz=CNC-BeiJing&dis_st=141&src=iqiyi.com&dis_hit=0&dis_tag=01010000&uuid=7b7370ec-63972aab-397&start=18385920&mss=1&qd_uid=1023108576&qd_k=d117275fbf0dbee1cbf8daeb7289fc1e&sd=0&qd_tm=1670851117507&qd_vip=0&cross-domain=1&pv=0.1&ssl=1&qd_sc=8f6fed51b33eb35cf3c29b520372481d&contentlength=516096&qyid=e25f31d1e250ba7bfb0e4929232b8498&qd_p=7b7370ec&qd_tvid=589243300&bid=500&qd_index=prv&qd_src=01010031010000000000&dis_src=tpa&stauto=1&qd_vipres=2&end=18902016&cphc=arta&ori=pcw1&num=1670851300437

"""

