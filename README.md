# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--20_05:56:51_UTC-green)

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

**Latest saved flight:** 2026-06-20 05:56:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-20 05:56:51 UTC

- **115,326** saved flights
- **39,973** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **115,326** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,402,504.6 tonnes** estimated CO2 emissions
- **81,304,613 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4754 |
| 2 | SkyWest Airlines | 4295 |
| 3 | EJA | 2237 |
| 4 | IndiGo | 2223 |
| 5 | American Airlines | 1805 |
| 6 | Southwest Airlines | 1715 |
| 7 | ENY | 1435 |
| 8 | Delta Air Lines | 1361 |
| 9 | Lufthansa | 1281 |
| 10 | Vueling | 1040 |
| 11 | WIF | 1022 |
| 12 | LATAM Airlines | 1014 |
| 13 | AZU | 964 |
| 14 | AXM | 953 |
| 15 | LXJ | 876 |
| 16 | Swiss International | 813 |
| 17 | All Nippon Airways | 792 |
| 18 | Alaska Airlines | 776 |
| 19 | QLK | 750 |
| 20 | easyJet | 740 |
| 21 | EJU | 723 |
| 22 | Cathay Pacific | 672 |
| 23 | AEE | 648 |
| 24 | United Airlines | 641 |
| 25 | VIV | 636 |
| 26 | Air France | 633 |
| 27 | CXK | 615 |
| 28 | MXY | 611 |
| 29 | AXB | 564 |
| 30 | GLO | 562 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 97401 |
| 2 | 🇪🇸 ES | 7859 |
| 3 | 🇮🇳 IN | 7013 |
| 4 | 🇦🇺 AU | 6857 |
| 5 | 🇧🇷 BR | 6356 |
| 6 | 🇮🇹 IT | 6175 |
| 7 | 🇩🇪 DE | 6150 |
| 8 | 🇨🇦 CA | 6071 |
| 9 | 🇯🇵 JP | 5180 |
| 10 | 🇬🇧 GB | 4995 |
| 11 | 🇫🇷 FR | 4578 |
| 12 | 🇨🇴 CO | 3972 |
| 13 | 🇲🇽 MX | 3396 |
| 14 | 🇬🇷 GR | 3291 |
| 15 | 🇳🇴 NO | 3179 |
| 16 | 🇨🇭 CH | 2929 |
| 17 | 🇲🇾 MY | 2470 |
| 18 | 🇹🇷 TR | 2328 |
| 19 | 🇿🇦 ZA | 1945 |
| 20 | 🇳🇿 NZ | 1899 |
| 21 | 🇵🇱 PL | 1886 |
| 22 | 🇰🇷 KR | 1882 |
| 23 | 🇹🇭 TH | 1879 |
| 24 | 🇵🇭 PH | 1680 |
| 25 | 🇬🇹 GT | 1634 |
| 26 | 🇲🇦 MA | 1254 |
| 27 | 🇲🇴 MO | 1168 |
| 28 | 🇲🇪 ME | 1134 |
| 29 | 🇳🇱 NL | 1116 |
| 30 | 🇭🇷 HR | 1000 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2440 |
| 2 | Denver International Airport |  | US | 1952 |
| 3 | Tokyo International Airport |  | JP | 1717 |
| 4 | Indira Gandhi International Airport |  | IN | 1534 |
| 5 | Guaymaral Airport |  | CO | 1470 |
| 6 | Harry Reid International Airport |  | US | 1448 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1417 |
| 8 | Zurich Airport |  | CH | 1284 |
| 9 | La Aurora Airport |  | GT | 1261 |
| 10 | Frankfurt am Main International Airport |  | DE | 1251 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1236 |
| 12 | El Dorado International Airport |  | CO | 1170 |
| 13 | Macau International Airport |  | MO | 1168 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1152 |
| 15 | Chicago O'Hare International Airport |  | US | 1134 |
| 16 | Capua Airport |  | IT | 1005 |
| 17 | Salt Lake City International Airport |  | US | 989 |
| 18 | Madrid Barajas International Airport |  | ES | 985 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 965 |
| 20 | Kuala Lumpur International Airport |  | MY | 954 |
| 21 | Charlotte/Douglas International Airport |  | US | 884 |
| 22 | Congonhas Airport |  | BR | 881 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 861 |
| 24 | Bengaluru International Airport |  | IN | 849 |
| 25 | Charles de Gaulle International Airport |  | FR | 846 |
| 26 | General Edward Lawrence Logan International Airport |  | US | 842 |
| 27 | Malpensa International Airport |  | IT | 824 |
| 28 | Ninoy Aquino International Airport |  | PH | 775 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 755 |
| 30 | Daniel K Inouye International Airport |  | US | 751 |
| 31 | Tenerife Norte Airport |  | ES | 750 |
| 32 | Barcelona International Airport |  | ES | 737 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 724 |
| 34 | Don Mueang International Airport |  | TH | 682 |
| 35 | Vitoria/Foronda Airport |  | ES | 679 |
| 36 | Calgary International Airport |  | CA | 678 |
| 37 | Amsterdam Airport Schiphol |  | NL | 678 |
| 38 | Seattle-Tacoma International Airport |  | US | 665 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 660 |
| 40 | Viracopos International Airport |  | BR | 658 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 610 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 417 | 21m | 244 km | 1,755.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 309 | 24m | 225 km | 1,198.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 298 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 286 | 1h 7m | 706 km | 3,482.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 282 | 1h 25m | 910 km | 4,425.2 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 8 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 275 | 1h 10m | 770 km | 3,653.2 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 231 | 26m | 275 km | 1,094.6 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 227 | 19m | 165 km | 645.7 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 214 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 173 | 22m | 55 km | 164.4 t |
| 14 | Bodø Airport (ENBO) | ENEN (ENEN) | 169 | 13m | - | - |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 168 | 20m | 99 km | 287.8 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 167 | 26m | 215 km | 618.5 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 157 | 27m | 152 km | 410.3 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 154 | 31m | 369 km | 980.2 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 152 | 44m | 452 km | 1,184.6 t |
| 21 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 151 | 44m | 241 km | 627.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 147 | 20m | 250 km | 635.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 147 | 18m | 144 km | 365.7 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 138 | 1h 1m | 695 km | 1,654.2 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 137 | 1h 44m | 1,423 km | 3,362.2 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 135 | 1h 39m | 1,156 km | 2,693.2 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 134 | 13m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 130 | 1h 17m | 961 km | 2,154.8 t |
| 30 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 129 | 24m | 223 km | 496.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| IAM2807 | IAM | Pratica Di Mare Airport (LIRE) | Rivolto Air Base (LIPI) | 2026-06-20 05:00 UTC | 2026-06-20 05:56 UTC | 56m |
| MEDIC01 | MED | Texel Airport (EHTX) | Leeuwarden Air Base (EHLW) | 2026-06-20 05:04 UTC | 2026-06-20 05:22 UTC | 17m |
| RPC7528 | RPC | Ninoy Aquino International Airport (RPLL) | San Fernando Airport (RPUS) | 2026-06-20 04:44 UTC | 2026-06-20 05:19 UTC | 34m |
| DLH899 | Lufthansa | Vilnius International Airport (EYVI) | Frankfurt am Main International Airport (EDDF) | 2026-06-20 03:32 UTC | 2026-06-20 05:16 UTC | 1h 44m |
| IMIAW | IMI | Sollieres Sardieres Airport (LFKD) | Sollieres Sardieres Airport (LFKD) | 2026-06-20 05:00 UTC | 2026-06-20 05:13 UTC | 13m |
| N401BA |  | Pueblo Memorial Airport (KPUB) | Rocky Mountain Metro Airport (KBJC) | 2026-06-20 03:49 UTC | 2026-06-20 05:11 UTC | 1h 22m |
| WZZ8025 | Wizz Air | Izgrev Airport (LBWV) | Hamburg Airport (EDDH) | 2026-06-20 02:42 UTC | 2026-06-20 05:10 UTC | 2h 28m |
| RYR7KL | Ryanair | Bari / Palese International Airport (LIBD) | Kasteli Airport (LGTL) | 2026-06-20 03:57 UTC | 2026-06-20 05:07 UTC | 1h 9m |
| ANZ852M | ANZ | Christchurch International Airport (NZCH) | Nelson Airport (NZNS) | 2026-06-20 04:19 UTC | 2026-06-20 05:07 UTC | 47m |
| IGO573E | IndiGo | Juhu Aerodrome (VAJJ) | Sarsawa Air Force Station (VISP) | 2026-06-20 03:23 UTC | 2026-06-20 05:05 UTC | 1h 41m |
| TWY188 | TWY | Montpellier-Mediterranee Airport (LFMT) | Nice-Cote d'Azur Airport (LFMN) | 2026-06-20 04:33 UTC | 2026-06-20 05:05 UTC | 31m |
| VOE7VT | VOE | Palermo / Punta Raisi Airport (LICJ) | Napoli / Capodichino International Airport (LIRN) | 2026-06-20 04:34 UTC | 2026-06-20 05:04 UTC | 30m |
| FDB9001 | flydubai | Al Maktoum International Airport (OMDW) | Al Maktoum International Airport (OMDW) | 2026-06-20 04:56 UTC | 2026-06-20 05:03 UTC | 7m |
| ASL57F | ASL | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 2026-06-20 04:44 UTC | 2026-06-20 05:03 UTC | 19m |
| RYR354V | Ryanair | Torino / Caselle International Airport (LIMF) | Capua Airport (LIAU) | 2026-06-20 04:07 UTC | 2026-06-20 05:02 UTC | 54m |
| ASA1102 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-06-20 04:40 UTC | 2026-06-20 05:01 UTC | 20m |
| IGO183E | IndiGo | Bengaluru International Airport (VOBL) | Giridih Airport (VE41) | 2026-06-20 02:59 UTC | 2026-06-20 05:00 UTC | 2h 0m |
| AWA473 | AWA | VGZR (VGZR) | Paro Airport (VQPR) | 2026-06-20 04:24 UTC | 2026-06-20 05:00 UTC | 35m |
| RSCU207 | RSC | Sydney Bankstown Airport (YSBK) | Wallacia Airport (YWLX) | 2026-06-20 04:11 UTC | 2026-06-20 05:00 UTC | 48m |
| N91SV |  | Dougherty Airport (1OH2) | Aerodrome Les Noyers Airport (50OH) | 2026-06-20 04:39 UTC | 2026-06-20 04:58 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
