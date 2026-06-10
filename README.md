# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--10_11:54:25_UTC-green)

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

**Latest saved flight:** 2026-06-10 11:54:25 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-10 11:54:25 UTC

- **107,329** saved flights
- **37,634** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **107,329** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,312,681.6 tonnes** estimated CO2 emissions
- **76,097,485 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4418 |
| 2 | SkyWest Airlines | 4031 |
| 3 | IndiGo | 2131 |
| 4 | EJA | 2069 |
| 5 | American Airlines | 1711 |
| 6 | Southwest Airlines | 1616 |
| 7 | ENY | 1341 |
| 8 | Delta Air Lines | 1274 |
| 9 | Lufthansa | 1230 |
| 10 | Vueling | 983 |
| 11 | LATAM Airlines | 954 |
| 12 | WIF | 941 |
| 13 | AXM | 914 |
| 14 | AZU | 875 |
| 15 | LXJ | 808 |
| 16 | Swiss International | 779 |
| 17 | All Nippon Airways | 747 |
| 18 | Alaska Airlines | 739 |
| 19 | QLK | 714 |
| 20 | easyJet | 693 |
| 21 | EJU | 683 |
| 22 | Cathay Pacific | 645 |
| 23 | AEE | 613 |
| 24 | VIV | 613 |
| 25 | Air France | 608 |
| 26 | United Airlines | 594 |
| 27 | MXY | 579 |
| 28 | CXK | 566 |
| 29 | Japan Airlines | 530 |
| 30 | AXB | 528 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 90275 |
| 2 | 🇪🇸 ES | 7368 |
| 3 | 🇮🇳 IN | 6715 |
| 4 | 🇦🇺 AU | 6430 |
| 5 | 🇧🇷 BR | 5919 |
| 6 | 🇩🇪 DE | 5760 |
| 7 | 🇮🇹 IT | 5750 |
| 8 | 🇨🇦 CA | 5612 |
| 9 | 🇯🇵 JP | 4900 |
| 10 | 🇬🇧 GB | 4561 |
| 11 | 🇫🇷 FR | 4272 |
| 12 | 🇨🇴 CO | 3715 |
| 13 | 🇲🇽 MX | 3213 |
| 14 | 🇬🇷 GR | 3050 |
| 15 | 🇳🇴 NO | 2967 |
| 16 | 🇨🇭 CH | 2734 |
| 17 | 🇲🇾 MY | 2343 |
| 18 | 🇹🇷 TR | 2087 |
| 19 | 🇿🇦 ZA | 1841 |
| 20 | 🇰🇷 KR | 1785 |
| 21 | 🇳🇿 NZ | 1783 |
| 22 | 🇹🇭 TH | 1763 |
| 23 | 🇵🇱 PL | 1751 |
| 24 | 🇵🇭 PH | 1572 |
| 25 | 🇬🇹 GT | 1550 |
| 26 | 🇲🇦 MA | 1186 |
| 27 | 🇲🇴 MO | 1123 |
| 28 | 🇳🇱 NL | 1052 |
| 29 | 🇲🇪 ME | 1035 |
| 30 | 🇭🇷 HR | 931 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2319 |
| 2 | Denver International Airport |  | US | 1823 |
| 3 | Tokyo International Airport |  | JP | 1623 |
| 4 | Indira Gandhi International Airport |  | IN | 1457 |
| 5 | Harry Reid International Airport |  | US | 1369 |
| 6 | Guaymaral Airport |  | CO | 1360 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1347 |
| 8 | Zurich Airport |  | CH | 1216 |
| 9 | Frankfurt am Main International Airport |  | DE | 1213 |
| 10 | La Aurora Airport |  | GT | 1192 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1159 |
| 12 | El Dorado International Airport |  | CO | 1129 |
| 13 | Macau International Airport |  | MO | 1123 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1079 |
| 15 | Chicago O'Hare International Airport |  | US | 1073 |
| 16 | Madrid Barajas International Airport |  | ES | 934 |
| 17 | Capua Airport |  | IT | 920 |
| 18 | Kuala Lumpur International Airport |  | MY | 918 |
| 19 | Salt Lake City International Airport |  | US | 913 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 913 |
| 21 | Charlotte/Douglas International Airport |  | US | 832 |
| 22 | Congonhas Airport |  | BR | 818 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 815 |
| 24 | Charles de Gaulle International Airport |  | FR | 812 |
| 25 | Bengaluru International Airport |  | IN | 811 |
| 26 | Malpensa International Airport |  | IT | 797 |
| 27 | Daniel K Inouye International Airport |  | US | 727 |
| 28 | Ninoy Aquino International Airport |  | PH | 721 |
| 29 | Tenerife Norte Airport |  | ES | 720 |
| 30 | Barcelona International Airport |  | ES | 703 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 698 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 697 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 697 |
| 34 | Amsterdam Airport Schiphol |  | NL | 650 |
| 35 | Don Mueang International Airport |  | TH | 645 |
| 36 | Vitoria/Foronda Airport |  | ES | 641 |
| 37 | Calgary International Airport |  | CA | 632 |
| 38 | Seattle-Tacoma International Airport |  | US | 621 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 617 |
| 40 | Netaji Subhash Chandra Bose International Airport |  | IN | 609 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 563 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 395 | 21m | 244 km | 1,663.2 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 285 | 24m | 225 km | 1,105.7 t |
| 4 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 282 | 1h 7m | 706 km | 3,433.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 279 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 274 | 14m | 114 km | 537.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 262 | 1h 25m | 910 km | 4,111.4 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 259 | 28m | 304 km | 1,357.7 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 249 | 1h 10m | 770 km | 3,307.8 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 221 | 19m | 165 km | 628.6 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 214 | 26m | 275 km | 1,014.1 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 207 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 162 | 20m | 99 km | 277.5 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 157 | 27m | 215 km | 581.5 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 155 | 22m | 55 km | 147.3 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 150 | 14m | 154 km | 397.4 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 149 | 27m | 152 km | 389.4 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 147 | 31m | 369 km | 935.7 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 146 | 13m | - | - |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 145 | 44m | 452 km | 1,130.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 140 | 18m | 144 km | 348.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 131 | 1h 1m | 695 km | 1,570.3 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 26 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 127 | 44m | 241 km | 527.5 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 126 | 1h 43m | 1,423 km | 3,092.2 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 121 | 1h 18m | 961 km | 2,005.6 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 121 | 1h 52m | 1,304 km | 2,722.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA801 | Cathay Pacific | Chicago O'Hare International Airport (KORD) | Macau International Airport (VMMC) | 2026-06-09 21:50 UTC | 2026-06-10 11:54 UTC | 14h 4m |
| ABX552 | ABX | Cincinnati/Northern Kentucky International Airport (KCVG) | John F Kennedy International Airport (KJFK) | 2026-06-10 10:08 UTC | 2026-06-10 11:45 UTC | 1h 36m |
| QTR62W | Qatar Airways | Edinburgh Airport (EGPH) | Queen Alia International Airport (OJAI) | 2026-06-10 07:12 UTC | 2026-06-10 11:39 UTC | 4h 26m |
| OYO5 | OYO | Poitiers-Biard Airport (LFBI) | Toulouse-Blagnac Airport (LFBO) | 2026-06-10 10:56 UTC | 2026-06-10 11:37 UTC | 40m |
| N944EV |  | Danville Regional Airport (KDAN) | Danville Regional Airport (KDAN) | 2026-06-10 11:17 UTC | 2026-06-10 11:34 UTC | 16m |
| WZZ128 | Wizz Air | Budapest Ferenc Liszt International Airport (LHBP) | Queen Alia International Airport (OJAI) | 2026-06-10 06:01 UTC | 2026-06-10 11:34 UTC | 5h 32m |
| CES5082 | China Eastern | Singapore Changi International Airport (WSSS) | Macau International Airport (VMMC) | 2026-06-10 04:51 UTC | 2026-06-10 11:29 UTC | 6h 38m |
| JANET33 | JAN | Harry Reid International Airport (KLAS) | KXTA (KXTA) | 2026-06-10 11:09 UTC | 2026-06-10 11:22 UTC | 12m |
| VEGA1 | VEG | Pirassununga Airport (SDPY) | Fazenda Boa Vista Airport (SSMV) | 2026-06-10 10:20 UTC | 2026-06-10 11:10 UTC | 50m |
| SEH5JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-06-10 10:41 UTC | 2026-06-10 11:07 UTC | 26m |
| FJKZH | FJK | Beynes Thiverval Airport (LFPF) | Chavenay Villepreux Airport (LFPX) | 2026-06-10 11:03 UTC | 2026-06-10 11:04 UTC | 1m |
| SFY7MB | SFY | Bournemouth Airport (EGHH) | Compton Abbas Aerodrome (EGHA) | 2026-06-10 10:08 UTC | 2026-06-10 11:04 UTC | 55m |
| RYR8XK | Ryanair | Bologna / Borgo Panigale Airport (LIPE) | Crotone Airport (LIBC) | 2026-06-10 09:58 UTC | 2026-06-10 11:02 UTC | 1h 3m |
| RYR65BP | Ryanair | Dublin Airport (EIDW) | Birmingham International Airport (EGBB) | 2026-06-10 10:22 UTC | 2026-06-10 11:01 UTC | 39m |
| WIF8HK | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-06-10 10:45 UTC | 2026-06-10 11:01 UTC | 15m |
| N724GT |  | Ocala International-Jim Taylor Field (KOCF) | Orlando Executive Airport (KORL) | 2026-06-10 10:42 UTC | 2026-06-10 10:59 UTC | 17m |
| CXK198 | CXK | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-06-10 09:35 UTC | 2026-06-10 10:58 UTC | 1h 23m |
| LLR513 | LLR | Bengaluru International Airport (VOBL) | Hosur Airport (VO95) | 2026-06-10 10:38 UTC | 2026-06-10 10:58 UTC | 19m |
| IGO6393 | IndiGo | Chhatrapati Shivaji International Airport (VABB) | Ambala Air Force Station (VIAM) | 2026-06-10 09:13 UTC | 2026-06-10 10:57 UTC | 1h 44m |
| RYR64BJ | Ryanair | Eindhoven Airport (EHEH) | Muchamiel Airport (LEMU) | 2026-06-10 08:55 UTC | 2026-06-10 10:57 UTC | 2h 1m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
