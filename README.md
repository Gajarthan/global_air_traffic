# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--21_10:51:12_UTC-green)

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

**Latest saved flight:** 2026-06-21 10:51:12 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-21 10:51:12 UTC

- **116,034** saved flights
- **40,171** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **116,034** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,411,112.8 tonnes** estimated CO2 emissions
- **81,803,642 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4791 |
| 2 | SkyWest Airlines | 4309 |
| 3 | EJA | 2246 |
| 4 | IndiGo | 2245 |
| 5 | American Airlines | 1813 |
| 6 | Southwest Airlines | 1726 |
| 7 | ENY | 1445 |
| 8 | Delta Air Lines | 1369 |
| 9 | Lufthansa | 1284 |
| 10 | Vueling | 1046 |
| 11 | WIF | 1025 |
| 12 | LATAM Airlines | 1019 |
| 13 | AZU | 966 |
| 14 | AXM | 957 |
| 15 | LXJ | 882 |
| 16 | Swiss International | 819 |
| 17 | All Nippon Airways | 798 |
| 18 | Alaska Airlines | 779 |
| 19 | QLK | 751 |
| 20 | easyJet | 742 |
| 21 | EJU | 729 |
| 22 | Cathay Pacific | 673 |
| 23 | AEE | 652 |
| 24 | VIV | 643 |
| 25 | United Airlines | 642 |
| 26 | Air France | 637 |
| 27 | CXK | 620 |
| 28 | MXY | 613 |
| 29 | AXB | 573 |
| 30 | GLO | 567 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 97963 |
| 2 | 🇪🇸 ES | 7908 |
| 3 | 🇮🇳 IN | 7073 |
| 4 | 🇦🇺 AU | 6882 |
| 5 | 🇧🇷 BR | 6387 |
| 6 | 🇮🇹 IT | 6209 |
| 7 | 🇩🇪 DE | 6183 |
| 8 | 🇨🇦 CA | 6090 |
| 9 | 🇯🇵 JP | 5225 |
| 10 | 🇬🇧 GB | 5055 |
| 11 | 🇫🇷 FR | 4612 |
| 12 | 🇨🇴 CO | 3985 |
| 13 | 🇲🇽 MX | 3418 |
| 14 | 🇬🇷 GR | 3314 |
| 15 | 🇳🇴 NO | 3189 |
| 16 | 🇨🇭 CH | 2963 |
| 17 | 🇲🇾 MY | 2487 |
| 18 | 🇹🇷 TR | 2352 |
| 19 | 🇿🇦 ZA | 1956 |
| 20 | 🇵🇱 PL | 1907 |
| 21 | 🇳🇿 NZ | 1905 |
| 22 | 🇰🇷 KR | 1888 |
| 23 | 🇹🇭 TH | 1885 |
| 24 | 🇵🇭 PH | 1690 |
| 25 | 🇬🇹 GT | 1637 |
| 26 | 🇲🇦 MA | 1261 |
| 27 | 🇲🇴 MO | 1169 |
| 28 | 🇲🇪 ME | 1141 |
| 29 | 🇳🇱 NL | 1119 |
| 30 | 🇭🇷 HR | 1012 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2448 |
| 2 | Denver International Airport |  | US | 1954 |
| 3 | Tokyo International Airport |  | JP | 1730 |
| 4 | Indira Gandhi International Airport |  | IN | 1552 |
| 5 | Guaymaral Airport |  | CO | 1475 |
| 6 | Harry Reid International Airport |  | US | 1453 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1420 |
| 8 | Zurich Airport |  | CH | 1292 |
| 9 | La Aurora Airport |  | GT | 1264 |
| 10 | Frankfurt am Main International Airport |  | DE | 1255 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1239 |
| 12 | El Dorado International Airport |  | CO | 1171 |
| 13 | Macau International Airport |  | MO | 1169 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1156 |
| 15 | Chicago O'Hare International Airport |  | US | 1140 |
| 16 | Capua Airport |  | IT | 1011 |
| 17 | Salt Lake City International Airport |  | US | 996 |
| 18 | Madrid Barajas International Airport |  | ES | 986 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 968 |
| 20 | Kuala Lumpur International Airport |  | MY | 962 |
| 21 | Congonhas Airport |  | BR | 887 |
| 22 | Charlotte/Douglas International Airport |  | US | 887 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 865 |
| 24 | Bengaluru International Airport |  | IN | 856 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 854 |
| 26 | Charles de Gaulle International Airport |  | FR | 851 |
| 27 | Malpensa International Airport |  | IT | 826 |
| 28 | Ninoy Aquino International Airport |  | PH | 780 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 758 |
| 30 | Daniel K Inouye International Airport |  | US | 757 |
| 31 | Tenerife Norte Airport |  | ES | 754 |
| 32 | Barcelona International Airport |  | ES | 740 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 731 |
| 34 | Don Mueang International Airport |  | TH | 684 |
| 35 | Vitoria/Foronda Airport |  | ES | 684 |
| 36 | Calgary International Airport |  | CA | 680 |
| 37 | Amsterdam Airport Schiphol |  | NL | 679 |
| 38 | Seattle-Tacoma International Airport |  | US | 667 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 660 |
| 40 | Scottsdale Airport |  | US | 659 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 612 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 422 | 21m | 244 km | 1,776.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 311 | 24m | 225 km | 1,206.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 299 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 285 | 1h 25m | 910 km | 4,472.3 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 8 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 279 | 1h 10m | 770 km | 3,706.3 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 261 | 28m | 304 km | 1,368.2 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 231 | 26m | 275 km | 1,094.6 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 230 | 19m | 165 km | 654.2 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 216 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 174 | 22m | 55 km | 165.4 t |
| 14 | Bodø Airport (ENBO) | ENEN (ENEN) | 169 | 13m | - | - |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 168 | 20m | 99 km | 287.8 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 167 | 26m | 215 km | 618.5 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 157 | 27m | 152 km | 410.3 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 154 | 31m | 369 km | 980.2 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 152 | 44m | 452 km | 1,184.6 t |
| 21 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 152 | 44m | 241 km | 631.4 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 147 | 20m | 250 km | 635.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 147 | 18m | 144 km | 365.7 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 143 | 1h 44m | 1,423 km | 3,509.4 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 139 | 1h 1m | 695 km | 1,666.2 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 136 | 13m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 135 | 1h 39m | 1,156 km | 2,693.2 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 132 | 1h 17m | 961 km | 2,188.0 t |
| 30 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 129 | 24m | 223 km | 496.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA654 | Cathay Pacific | Suvarnabhumi Airport (VTBS) | Chek Lap Kok International Airport (VHHH) | 2026-06-21 08:26 UTC | 2026-06-21 10:51 UTC | 2h 24m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-06-21 10:02 UTC | 2026-06-21 10:37 UTC | 34m |
| HBPRR | HBP | Lucca / Tassignano Airport (LIQL) | Aosta Airport (LIMW) | 2026-06-21 09:14 UTC | 2026-06-21 10:34 UTC | 1h 20m |
| DLA9800 | DLA | Pula Airport (LDPL) | Pula Airport (LDPL) | 2026-06-21 10:07 UTC | 2026-06-21 10:33 UTC | 26m |
| LOG85CB | LOG | Isle of Man Airport (EGNS) | Birmingham International Airport (EGBB) | 2026-06-21 09:51 UTC | 2026-06-21 10:32 UTC | 40m |
| CXK237 | CXK | Essex County Airport (KCDW) | Lancaster Airport (KLNS) | 2026-06-21 09:13 UTC | 2026-06-21 10:27 UTC | 1h 13m |
| RYR9WQ | Ryanair | Liverpool John Lennon Airport (EGGP) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-06-21 08:08 UTC | 2026-06-21 10:22 UTC | 2h 14m |
| SXS7RR | SXS | Zurich Airport (LSZH) | Kaklic Airport (LTFA) | 2026-06-21 07:59 UTC | 2026-06-21 10:16 UTC | 2h 17m |
| EJU18AD | EJU | Mollis Airport (LSZM) | L'Aquila / Preturo Airport (LIAP) | 2026-06-21 08:51 UTC | 2026-06-21 10:16 UTC | 1h 24m |
| MAS613 | Malaysia Airlines | Kuala Lumpur International Airport (WMKK) | Hang Nadim Airport (WIDD) | 2026-06-21 09:26 UTC | 2026-06-21 10:15 UTC | 49m |
| SIA115 | Singapore Airlines | Kuala Lumpur International Airport (WMKK) | Hang Nadim Airport (WIDD) | 2026-06-21 09:23 UTC | 2026-06-21 10:14 UTC | 51m |
| KAL643 | Korean Air | Incheon International Airport (RKSI) | Pulau Tioman Airport (WMBT) | 2026-06-21 05:01 UTC | 2026-06-21 10:13 UTC | 5h 12m |
| TCMKA | TCM | Ataturk International Airport (LTBA) | Etimesgut Air Base (LTAD) | 2026-06-21 09:37 UTC | 2026-06-21 10:13 UTC | 35m |
| RYR9WK | Ryanair | Chania International Airport (LGSA) | Ihtiman Airport (LBHT) | 2026-06-21 09:08 UTC | 2026-06-21 10:12 UTC | 1h 4m |
| FIN1143 | Finnair | Helsinki Vantaa Airport (EFHK) | Khrabrovo Airport (UMKK) | 2026-06-21 09:19 UTC | 2026-06-21 10:12 UTC | 52m |
| RYR33NV | Ryanair | Edinburgh Airport (EGPH) | Teruel Airport (LETL) | 2026-06-21 07:50 UTC | 2026-06-21 10:12 UTC | 2h 21m |
| WWF170 | WWF | Sierraville Dearwater Airport (KO79) | CA38 (CA38) | 2026-06-21 10:00 UTC | 2026-06-21 10:12 UTC | 11m |
| AAL951 | American Airlines | John F Kennedy International Airport (KJFK) | Atibaia Airport (SDTB) | 2026-06-21 01:15 UTC | 2026-06-21 10:12 UTC | 8h 56m |
| IGO6226 | IndiGo | Indira Gandhi International Airport (VIDP) | Dehradun Airport (VIDN) | 2026-06-21 09:48 UTC | 2026-06-21 10:12 UTC | 23m |
| ZKIDU | ZKI | Invercargill Airport (NZNV) | Invercargill Airport (NZNV) | 2026-06-21 10:08 UTC | 2026-06-21 10:11 UTC | 2m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
