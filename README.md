# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--12_04:45:30_UTC-green)

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

**Latest saved flight:** 2026-06-12 04:45:30 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-12 04:45:30 UTC

- **108,605** saved flights
- **38,006** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **108,605** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,328,016.4 tonnes** estimated CO2 emissions
- **76,986,455 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4468 |
| 2 | SkyWest Airlines | 4068 |
| 3 | IndiGo | 2151 |
| 4 | EJA | 2092 |
| 5 | American Airlines | 1723 |
| 6 | Southwest Airlines | 1633 |
| 7 | ENY | 1355 |
| 8 | Delta Air Lines | 1288 |
| 9 | Lufthansa | 1234 |
| 10 | Vueling | 992 |
| 11 | LATAM Airlines | 962 |
| 12 | WIF | 953 |
| 13 | AXM | 923 |
| 14 | AZU | 891 |
| 15 | LXJ | 821 |
| 16 | Swiss International | 788 |
| 17 | All Nippon Airways | 752 |
| 18 | Alaska Airlines | 742 |
| 19 | QLK | 723 |
| 20 | easyJet | 700 |
| 21 | EJU | 691 |
| 22 | Cathay Pacific | 654 |
| 23 | VIV | 618 |
| 24 | AEE | 617 |
| 25 | Air France | 613 |
| 26 | United Airlines | 598 |
| 27 | MXY | 584 |
| 28 | CXK | 572 |
| 29 | Japan Airlines | 537 |
| 30 | AXB | 533 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 91441 |
| 2 | 🇪🇸 ES | 7442 |
| 3 | 🇮🇳 IN | 6774 |
| 4 | 🇦🇺 AU | 6506 |
| 5 | 🇧🇷 BR | 5988 |
| 6 | 🇩🇪 DE | 5829 |
| 7 | 🇮🇹 IT | 5806 |
| 8 | 🇨🇦 CA | 5701 |
| 9 | 🇯🇵 JP | 4938 |
| 10 | 🇬🇧 GB | 4604 |
| 11 | 🇫🇷 FR | 4323 |
| 12 | 🇨🇴 CO | 3740 |
| 13 | 🇲🇽 MX | 3252 |
| 14 | 🇬🇷 GR | 3075 |
| 15 | 🇳🇴 NO | 3001 |
| 16 | 🇨🇭 CH | 2765 |
| 17 | 🇲🇾 MY | 2363 |
| 18 | 🇹🇷 TR | 2107 |
| 19 | 🇿🇦 ZA | 1849 |
| 20 | 🇰🇷 KR | 1811 |
| 21 | 🇳🇿 NZ | 1796 |
| 22 | 🇹🇭 TH | 1784 |
| 23 | 🇵🇱 PL | 1771 |
| 24 | 🇵🇭 PH | 1595 |
| 25 | 🇬🇹 GT | 1557 |
| 26 | 🇲🇦 MA | 1194 |
| 27 | 🇲🇴 MO | 1142 |
| 28 | 🇳🇱 NL | 1072 |
| 29 | 🇲🇪 ME | 1047 |
| 30 | 🇭🇷 HR | 949 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2340 |
| 2 | Denver International Airport |  | US | 1834 |
| 3 | Tokyo International Airport |  | JP | 1635 |
| 4 | Indira Gandhi International Airport |  | IN | 1474 |
| 5 | Harry Reid International Airport |  | US | 1381 |
| 6 | Guaymaral Airport |  | CO | 1379 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1354 |
| 8 | Zurich Airport |  | CH | 1229 |
| 9 | Frankfurt am Main International Airport |  | DE | 1217 |
| 10 | La Aurora Airport |  | GT | 1199 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1165 |
| 12 | Macau International Airport |  | MO | 1142 |
| 13 | El Dorado International Airport |  | CO | 1132 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1091 |
| 15 | Chicago O'Hare International Airport |  | US | 1077 |
| 16 | Madrid Barajas International Airport |  | ES | 941 |
| 17 | Capua Airport |  | IT | 934 |
| 18 | Kuala Lumpur International Airport |  | MY | 926 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 923 |
| 20 | Salt Lake City International Airport |  | US | 919 |
| 21 | Charlotte/Douglas International Airport |  | US | 841 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 830 |
| 23 | Congonhas Airport |  | BR | 827 |
| 24 | Charles de Gaulle International Airport |  | FR | 819 |
| 25 | Bengaluru International Airport |  | IN | 818 |
| 26 | Malpensa International Airport |  | IT | 800 |
| 27 | Ninoy Aquino International Airport |  | PH | 733 |
| 28 | Daniel K Inouye International Airport |  | US | 730 |
| 29 | Tenerife Norte Airport |  | ES | 726 |
| 30 | General Edward Lawrence Logan International Airport |  | US | 713 |
| 31 | Barcelona International Airport |  | ES | 712 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 706 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 700 |
| 34 | Amsterdam Airport Schiphol |  | NL | 662 |
| 35 | Don Mueang International Airport |  | TH | 651 |
| 36 | Vitoria/Foronda Airport |  | ES | 647 |
| 37 | Calgary International Airport |  | CA | 641 |
| 38 | Norman Y Mineta San Jose International Airport |  | US | 625 |
| 39 | Seattle-Tacoma International Airport |  | US | 625 |
| 40 | Viracopos International Airport |  | BR | 614 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 571 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 398 | 21m | 244 km | 1,675.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 292 | 24m | 225 km | 1,132.8 t |
| 4 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 283 | 1h 7m | 706 km | 3,445.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 282 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 274 | 14m | 114 km | 537.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 264 | 1h 25m | 910 km | 4,142.8 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 251 | 1h 10m | 770 km | 3,334.3 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 221 | 19m | 165 km | 628.6 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 217 | 26m | 275 km | 1,028.3 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 208 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 162 | 20m | 99 km | 277.5 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 159 | 22m | 55 km | 151.1 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 158 | 27m | 215 km | 585.2 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 153 | 14m | 154 km | 405.4 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 150 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 150 | 27m | 152 km | 392.0 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 147 | 31m | 369 km | 935.7 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 145 | 44m | 452 km | 1,130.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 140 | 18m | 144 km | 348.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 132 | 1h 1m | 695 km | 1,582.3 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 26 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 130 | 44m | 241 km | 540.0 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 128 | 1h 43m | 1,423 km | 3,141.3 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 123 | 1h 17m | 961 km | 2,038.8 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 30 | Calgary International Airport (CYYC) | Moose Jaw Municipal Airport (CJS4) | 121 | 1h 2m | 611 km | 1,276.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N64FB |  | Sacramento Mather Airport (KMHR) | Sacramento Mather Airport (KMHR) | 2026-06-12 04:26 UTC | 2026-06-12 04:45 UTC | 19m |
| DESERT8 | DES | Lake Havasu City Airport (KHII) | Lake Havasu City Airport (KHII) | 2026-06-12 03:59 UTC | 2026-06-12 04:37 UTC | 37m |
| IXIAN | IXI | Raron Airport (LSTA) | Raron Airport (LSTA) | 2026-06-12 04:03 UTC | 2026-06-12 04:27 UTC | 23m |
| SWA1839 | Southwest Airlines | Mahlon Sweet Field (KEUG) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-06-12 02:58 UTC | 2026-06-12 04:07 UTC | 1h 8m |
| N621TK |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-06-12 03:38 UTC | 2026-06-12 04:06 UTC | 28m |
| N65KL |  | Santa Lucia Air Force Base (MMSM) | Toronto Pearson International Airport (CYYZ) | 2026-06-11 23:59 UTC | 2026-06-12 04:01 UTC | 4h 2m |
| J977KT |  | Adi Sutjipto International Airport (WARJ) | Adi Sutjipto International Airport (WARJ) | 2026-06-12 03:24 UTC | 2026-06-12 04:01 UTC | 36m |
| JHH | JHH | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-06-12 03:39 UTC | 2026-06-12 03:54 UTC | 15m |
| DRGN23 | DRG | RAAF Base Amberley (YAMB) | Melbourne International Airport (YMML) | 2026-06-12 01:09 UTC | 2026-06-12 03:50 UTC | 2h 41m |
| C6040 |  | San Diego International Airport (KSAN) | San Diego International Airport (KSAN) | 2026-06-12 03:27 UTC | 2026-06-12 03:45 UTC | 18m |
| N617DA |  | Coeur D'Alene/Pappy Boyington Field (KCOE) | White Pine Flats Ranch Llc Airport (ID94) | 2026-06-12 03:16 UTC | 2026-06-12 03:43 UTC | 27m |
| OGN207 | OGN | Palmerston North Airport (NZPM) | Wellington International Airport (NZWN) | 2026-06-12 03:20 UTC | 2026-06-12 03:42 UTC | 21m |
| GRIT84 | GRI | Laramie Regional Airport (KLAR) | Laramie Regional Airport (KLAR) | 2026-06-12 03:38 UTC | 2026-06-12 03:40 UTC | 1m |
| AXM6040 | AXM | Kuala Lumpur International Airport (WMKK) | Kluang Airport (WMAP) | 2026-06-12 03:21 UTC | 2026-06-12 03:37 UTC | 16m |
| N786AC |  | Boise Air Trml/Gowen Field (KBOI) | Black Butte Ranch Airport (0ID4) | 2026-06-12 03:18 UTC | 2026-06-12 03:36 UTC | 18m |
| VOI3296 | VOI | General Abelardo L. Rodriguez International Airport (MMTJ) | Atizapan De Zaragoza Airport (MMJC) | 2026-06-12 00:40 UTC | 2026-06-12 03:34 UTC | 2h 53m |
| LR441 |  | Brisbane International Airport (YBBN) | Gayndah Airport (YGAY) | 2026-06-12 02:58 UTC | 2026-06-12 03:32 UTC | 33m |
| EJA942 | EJA | Denver International Airport (KDEN) | Oakland San Francisco Bay Airport (KOAK) | 2026-06-12 01:10 UTC | 2026-06-12 03:31 UTC | 2h 20m |
| JST890 | JST | Sydney Kingsford Smith International Airport (YSSY) | Maryborough Airport (YMYB) | 2026-06-12 02:14 UTC | 2026-06-12 03:30 UTC | 1h 15m |
| SWA4875 | Southwest Airlines | San Diego International Airport (KSAN) | NV13 (NV13) | 2026-06-12 02:24 UTC | 2026-06-12 03:27 UTC | 1h 3m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
