# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--18_06:14:44_UTC-green)

![Flight Map](images/flight_map.png)

## About

Historical archive of saved air traffic routes collected from the [OpenSky Network](https://opensky-network.org/) API. This repository keeps appending completed flights to `data/flights/` and rebuilds the visuals from the full archive.

**Data Source:** Saved route files in `data/flights/` (originally fetched from OpenSky `/flights/all`)

**Update Frequency:** Every 5 minutes via GitHub Actions

**How it works:**
- Fetches recently completed routes from OpenSky
- Saves each route as a JSON file in `data/flights/`
- Rebuilds aggregate statistics from all saved historical routes
- Generates a historical route map and archive summary
- Generates daily reports, weekly leaderboards, and timelapse GIFs

## Route Timelapse

![Timelapse](images/timelapse.gif)

## Archive Snapshot

**Latest saved flight:** 2026-06-18 06:14:44 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-18 06:14:44 UTC

- **113,751** saved flights
- **39,496** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **113,751** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,386,027.9 tonnes** estimated CO2 emissions
- **80,349,440 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4686 |
| 2 | SkyWest Airlines | 4238 |
| 3 | EJA | 2204 |
| 4 | IndiGo | 2203 |
| 5 | American Airlines | 1792 |
| 6 | Southwest Airlines | 1692 |
| 7 | ENY | 1416 |
| 8 | Delta Air Lines | 1342 |
| 9 | Lufthansa | 1271 |
| 10 | Vueling | 1033 |
| 11 | WIF | 1009 |
| 12 | LATAM Airlines | 1003 |
| 13 | AZU | 952 |
| 14 | AXM | 947 |
| 15 | LXJ | 865 |
| 16 | Swiss International | 810 |
| 17 | All Nippon Airways | 788 |
| 18 | Alaska Airlines | 769 |
| 19 | QLK | 744 |
| 20 | easyJet | 731 |
| 21 | EJU | 716 |
| 22 | Cathay Pacific | 668 |
| 23 | AEE | 638 |
| 24 | VIV | 630 |
| 25 | Air France | 629 |
| 26 | United Airlines | 629 |
| 27 | MXY | 603 |
| 28 | CXK | 602 |
| 29 | AXB | 557 |
| 30 | GLO | 557 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 95920 |
| 2 | 🇪🇸 ES | 7757 |
| 3 | 🇮🇳 IN | 6951 |
| 4 | 🇦🇺 AU | 6783 |
| 5 | 🇧🇷 BR | 6295 |
| 6 | 🇮🇹 IT | 6104 |
| 7 | 🇩🇪 DE | 6080 |
| 8 | 🇨🇦 CA | 5977 |
| 9 | 🇯🇵 JP | 5138 |
| 10 | 🇬🇧 GB | 4906 |
| 11 | 🇫🇷 FR | 4520 |
| 12 | 🇨🇴 CO | 3867 |
| 13 | 🇲🇽 MX | 3359 |
| 14 | 🇬🇷 GR | 3236 |
| 15 | 🇳🇴 NO | 3146 |
| 16 | 🇨🇭 CH | 2904 |
| 17 | 🇲🇾 MY | 2449 |
| 18 | 🇹🇷 TR | 2284 |
| 19 | 🇿🇦 ZA | 1927 |
| 20 | 🇳🇿 NZ | 1877 |
| 21 | 🇰🇷 KR | 1874 |
| 22 | 🇵🇱 PL | 1857 |
| 23 | 🇹🇭 TH | 1853 |
| 24 | 🇵🇭 PH | 1657 |
| 25 | 🇬🇹 GT | 1622 |
| 26 | 🇲🇦 MA | 1245 |
| 27 | 🇲🇴 MO | 1165 |
| 28 | 🇲🇪 ME | 1116 |
| 29 | 🇳🇱 NL | 1103 |
| 30 | 🇭🇷 HR | 990 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2419 |
| 2 | Denver International Airport |  | US | 1928 |
| 3 | Tokyo International Airport |  | JP | 1706 |
| 4 | Indira Gandhi International Airport |  | IN | 1515 |
| 5 | Guaymaral Airport |  | CO | 1431 |
| 6 | Harry Reid International Airport |  | US | 1427 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1399 |
| 8 | Zurich Airport |  | CH | 1278 |
| 9 | La Aurora Airport |  | GT | 1251 |
| 10 | Frankfurt am Main International Airport |  | DE | 1240 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1220 |
| 12 | Macau International Airport |  | MO | 1165 |
| 13 | El Dorado International Airport |  | CO | 1153 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1139 |
| 15 | Chicago O'Hare International Airport |  | US | 1123 |
| 16 | Capua Airport |  | IT | 988 |
| 17 | Madrid Barajas International Airport |  | ES | 981 |
| 18 | Salt Lake City International Airport |  | US | 966 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 957 |
| 20 | Kuala Lumpur International Airport |  | MY | 949 |
| 21 | Charlotte/Douglas International Airport |  | US | 882 |
| 22 | Congonhas Airport |  | BR | 872 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 852 |
| 24 | Bengaluru International Airport |  | IN | 842 |
| 25 | Charles de Gaulle International Airport |  | FR | 841 |
| 26 | Malpensa International Airport |  | IT | 818 |
| 27 | General Edward Lawrence Logan International Airport |  | US | 805 |
| 28 | Ninoy Aquino International Airport |  | PH | 764 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 748 |
| 30 | Daniel K Inouye International Airport |  | US | 746 |
| 31 | Tenerife Norte Airport |  | ES | 741 |
| 32 | Barcelona International Airport |  | ES | 733 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 716 |
| 34 | Amsterdam Airport Schiphol |  | NL | 674 |
| 35 | Don Mueang International Airport |  | TH | 673 |
| 36 | Vitoria/Foronda Airport |  | ES | 672 |
| 37 | Calgary International Airport |  | CA | 670 |
| 38 | Seattle-Tacoma International Airport |  | US | 654 |
| 39 | Viracopos International Airport |  | BR | 651 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 650 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 593 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 412 | 21m | 244 km | 1,734.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 304 | 24m | 225 km | 1,179.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 297 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 285 | 1h 7m | 706 km | 3,469.9 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 280 | 1h 25m | 910 km | 4,393.9 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 277 | 14m | 114 km | 543.3 t |
| 8 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 272 | 1h 10m | 770 km | 3,613.3 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 228 | 26m | 275 km | 1,080.4 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 226 | 19m | 165 km | 642.9 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 212 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 168 | 20m | 99 km | 287.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 166 | 26m | 215 km | 614.8 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 166 | 22m | 55 km | 157.8 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 164 | 13m | - | - |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 155 | 27m | 152 km | 405.1 t |
| 18 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 153 | 31m | 369 km | 973.9 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 151 | 44m | 452 km | 1,176.8 t |
| 21 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 147 | 44m | 241 km | 610.6 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 147 | 18m | 144 km | 365.7 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 145 | 20m | 250 km | 626.3 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 136 | 1h 1m | 695 km | 1,630.2 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 134 | 1h 43m | 1,423 km | 3,288.6 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 133 | 1h 39m | 1,156 km | 2,653.3 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 128 | 12m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 127 | 1h 17m | 961 km | 2,105.1 t |
| 30 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 126 | 24m | 223 km | 484.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LNPFF | LNP | Kjeller Airport (ENKJ) | Kjeller Airport (ENKJ) | 2026-06-18 06:00 UTC | 2026-06-18 06:14 UTC | 14m |
| N2348K |  | UT99 (UT99) | Wendover Airport (KENV) | 2026-06-18 04:22 UTC | 2026-06-18 05:59 UTC | 1h 37m |
| CHG855 | CHG | Liege Airport (EBLG) | Macau International Airport (VMMC) | 2026-06-17 19:06 UTC | 2026-06-18 05:56 UTC | 10h 49m |
| JON07 | JON | Ostersund Airport (ESNZ) | Arvidsjaur Airport (ESNX) | 2026-06-18 05:31 UTC | 2026-06-18 05:55 UTC | 24m |
| 5YDRY |  | Jomo Kenyatta International Airport (HKJK) | Nairobi Wilson Airport (HKNW) | 2026-06-18 05:53 UTC | 2026-06-18 05:54 UTC | 0m |
| ETH736 | Ethiopian Airlines | Malpensa International Airport (LIMC) | Zurich Airport (LSZH) | 2026-06-18 05:13 UTC | 2026-06-18 05:52 UTC | 39m |
| XCN81 | XCN | Spokane International Airport (KGEG) | Sunnyside Municipal Airport (K1S5) | 2026-06-18 05:16 UTC | 2026-06-18 05:51 UTC | 34m |
| HARR85 | HAR | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-06-18 04:45 UTC | 2026-06-18 05:42 UTC | 56m |
| N481U |  | Ted Stevens Anchorage International Airport (PANC) | Birchwood Airport (PABV) | 2026-06-18 05:25 UTC | 2026-06-18 05:42 UTC | 16m |
| IGO1721 | IndiGo | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-06-18 00:55 UTC | 2026-06-18 05:41 UTC | 4h 46m |
| N3524F |  | Ogden-Hinckley Airport (KOGD) | Preston Airport (KU10) | 2026-06-18 05:13 UTC | 2026-06-18 05:40 UTC | 27m |
| AM280 |  | Sydney Kingsford Smith International Airport (YSSY) | Cudal Airport (YCUA) | 2026-06-18 05:04 UTC | 2026-06-18 05:40 UTC | 35m |
| DLH5KA | Lufthansa | Frankfurt am Main International Airport (EDDF) | Neustadt/Aisch Airport (EDQN) | 2026-06-18 05:16 UTC | 2026-06-18 05:38 UTC | 22m |
| VAA010 | VAA | Mukhrani Airport (UGMM) | UGMS (UGMS) | 2026-06-18 05:01 UTC | 2026-06-18 05:35 UTC | 33m |
| GNS103 | GNS | Al Udeid Air Base (OTBH) | Al Udeid Air Base (OTBH) | 2026-06-18 05:17 UTC | 2026-06-18 05:34 UTC | 17m |
| EWG6KW | EWG | Berlin Brandenburg Airport (EDDB) | Cologne Bonn Airport (EDDK) | 2026-06-18 04:40 UTC | 2026-06-18 05:34 UTC | 53m |
| CPA740 | Cathay Pacific | Noi Bai International Airport (VVNB) | Macau International Airport (VMMC) | 2026-06-18 04:23 UTC | 2026-06-18 05:34 UTC | 1h 10m |
| AEE348 | AEE | Eleftherios Venizelos International Airport (LGAV) | Kasteli Airport (LGTL) | 2026-06-18 05:11 UTC | 2026-06-18 05:30 UTC | 19m |
| AZG922 | AZG | Frankfurt-Hahn Airport (EDFH) | Macau International Airport (VMMC) | 2026-06-17 12:17 UTC | 2026-06-18 05:28 UTC | 17h 11m |
| AMF | AMF | Perth Jandakot Airport (YPJT) | Morawa Airport (YMRW) | 2026-06-18 04:39 UTC | 2026-06-18 05:26 UTC | 46m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
