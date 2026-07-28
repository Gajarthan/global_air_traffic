# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--28_22:22:37_UTC-green)

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

**Latest saved flight:** 2026-07-28 22:22:37 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-28 22:22:37 UTC

- **157,413** saved flights
- **52,249** unique routes
- **136** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **157,413** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,888,417.8 tonnes** estimated CO2 emissions
- **109,473,498 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6333 |
| 2 | SkyWest Airlines | 5769 |
| 3 | EJA | 3118 |
| 4 | IndiGo | 2775 |
| 5 | American Airlines | 2512 |
| 6 | Southwest Airlines | 2473 |
| 7 | ENY | 1965 |
| 8 | Delta Air Lines | 1870 |
| 9 | Lufthansa | 1507 |
| 10 | LATAM Airlines | 1469 |
| 11 | AZU | 1381 |
| 12 | WIF | 1328 |
| 13 | Vueling | 1321 |
| 14 | LXJ | 1214 |
| 15 | AXM | 1102 |
| 16 | Swiss International | 1090 |
| 17 | easyJet | 1028 |
| 18 | Alaska Airlines | 986 |
| 19 | QLK | 974 |
| 20 | All Nippon Airways | 973 |
| 21 | EJU | 966 |
| 22 | VIV | 863 |
| 23 | United Airlines | 837 |
| 24 | CXK | 836 |
| 25 | Cathay Pacific | 826 |
| 26 | GLO | 826 |
| 27 | AEE | 824 |
| 28 | MXY | 819 |
| 29 | JetBlue | 817 |
| 30 | Air France | 816 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 135933 |
| 2 | 🇪🇸 ES | 10143 |
| 3 | 🇧🇷 BR | 8982 |
| 4 | 🇦🇺 AU | 8863 |
| 5 | 🇮🇳 IN | 8729 |
| 6 | 🇨🇦 CA | 8514 |
| 7 | 🇮🇹 IT | 8124 |
| 8 | 🇩🇪 DE | 7973 |
| 9 | 🇬🇧 GB | 7233 |
| 10 | 🇯🇵 JP | 6420 |
| 11 | 🇫🇷 FR | 6218 |
| 12 | 🇨🇴 CO | 5526 |
| 13 | 🇲🇽 MX | 4517 |
| 14 | 🇬🇷 GR | 4488 |
| 15 | 🇳🇴 NO | 4162 |
| 16 | 🇨🇭 CH | 4115 |
| 17 | 🇹🇷 TR | 3762 |
| 18 | 🇲🇾 MY | 2871 |
| 19 | 🇵🇱 PL | 2683 |
| 20 | 🇿🇦 ZA | 2546 |
| 21 | 🇳🇿 NZ | 2335 |
| 22 | 🇹🇭 TH | 2261 |
| 23 | 🇰🇷 KR | 2091 |
| 24 | 🇵🇭 PH | 2066 |
| 25 | 🇬🇹 GT | 2021 |
| 26 | 🇲🇦 MA | 1605 |
| 27 | 🇲🇪 ME | 1517 |
| 28 | 🇭🇷 HR | 1453 |
| 29 | 🇳🇱 NL | 1434 |
| 30 | 🇲🇴 MO | 1296 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3237 |
| 2 | Denver International Airport |  | US | 2639 |
| 3 | Tokyo International Airport |  | JP | 2035 |
| 4 | Guaymaral Airport |  | CO | 1978 |
| 5 | Indira Gandhi International Airport |  | IN | 1944 |
| 6 | Harry Reid International Airport |  | US | 1924 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1743 |
| 8 | Zurich Airport |  | CH | 1692 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1654 |
| 10 | La Aurora Airport |  | GT | 1567 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1470 |
| 12 | Frankfurt am Main International Airport |  | DE | 1457 |
| 13 | El Dorado International Airport |  | CO | 1433 |
| 14 | Chicago O'Hare International Airport |  | US | 1432 |
| 15 | Salt Lake City International Airport |  | US | 1418 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1324 |
| 17 | Macau International Airport |  | MO | 1296 |
| 18 | Congonhas Airport |  | BR | 1292 |
| 19 | Madrid Barajas International Airport |  | ES | 1250 |
| 20 | Capua Airport |  | IT | 1237 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1209 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1124 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1121 |
| 24 | Charlotte/Douglas International Airport |  | US | 1114 |
| 25 | Kuala Lumpur International Airport |  | MY | 1099 |
| 26 | Charles de Gaulle International Airport |  | FR | 1078 |
| 27 | Bengaluru International Airport |  | IN | 1037 |
| 28 | Malpensa International Airport |  | IT | 1035 |
| 29 | Ninoy Aquino International Airport |  | PH | 968 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 960 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 950 |
| 32 | Barcelona International Airport |  | ES | 941 |
| 33 | Daniel K Inouye International Airport |  | US | 928 |
| 34 | Seattle-Tacoma International Airport |  | US | 918 |
| 35 | Calgary International Airport |  | CA | 903 |
| 36 | Tenerife Norte Airport |  | ES | 894 |
| 37 | Viracopos International Airport |  | BR | 893 |
| 38 | Scottsdale Airport |  | US | 890 |
| 39 | Oslo Gardermoen Airport |  | NO | 871 |
| 40 | Amsterdam Airport Schiphol |  | NL | 865 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 830 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 567 | 21m | 244 km | 2,387.5 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 376 | 24m | 225 km | 1,458.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 376 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 361 | 1h 9m | 770 km | 4,795.6 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 288 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 277 | 27m | 275 km | 1,312.6 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 233 | 22m | 55 km | 221.5 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 220 | 44m | 241 km | 913.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 213 | 1h 47m | 1,423 km | 5,227.4 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 206 | 26m | 215 km | 762.9 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 202 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 202 | 20m | 99 km | 346.0 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 199 | 20m | 250 km | 859.6 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 189 | 30m | 49 km | 159.8 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 188 | 27m | 152 km | 491.3 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 187 | 18m | 144 km | 465.2 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 186 | 1h 15m | 961 km | 3,083.0 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 183 | 12m | - | - |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 182 | 31m | 369 km | 1,158.5 t |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 178 | 50m | 556 km | 1,706.3 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 176 | 1h 39m | 1,156 km | 3,511.1 t |
| 28 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 176 | 44m | 452 km | 1,371.7 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 174 | 1h 1m | 695 km | 2,085.7 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 166 | 1h 50m | 1,304 km | 3,734.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA372 | Cathay Pacific | Madrid Barajas International Airport (LEMD) | Zhuhai Airport (ZGSD) | 2026-07-28 10:53 UTC | 2026-07-28 22:22 UTC | 11h 29m |
| CPA300 | Cathay Pacific | Munich International Airport (EDDM) | Zhuhai Airport (ZGSD) | 2026-07-28 12:10 UTC | 2026-07-28 22:19 UTC | 10h 8m |
| CPA382 | Cathay Pacific | Zurich Airport (LSZH) | Zhuhai Airport (ZGSD) | 2026-07-28 11:59 UTC | 2026-07-28 22:18 UTC | 10h 19m |
| N6265T |  | Chicago Executive Airport (KPWK) | Waukegan Ntl Airport (KUGN) | 2026-07-28 21:48 UTC | 2026-07-28 22:18 UTC | 30m |
| CKS703 | CKS | Ben Gurion International Airport (LLBG) | Zhuhai Airport (ZGSD) | 2026-07-28 13:11 UTC | 2026-07-28 22:16 UTC | 9h 4m |
| N18JA |  | Aurora Municipal Airport (KARR) | Humm Airport (06IL) | 2026-07-28 22:03 UTC | 2026-07-28 22:15 UTC | 12m |
| N740SC |  | El Peco Ranch Airport (49CL) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-07-28 21:50 UTC | 2026-07-28 22:15 UTC | 25m |
| CPA640 | Cathay Pacific | Tribhuvan International Airport (VNKT) | Macau International Airport (VMMC) | 2026-07-28 18:29 UTC | 2026-07-28 22:13 UTC | 3h 44m |
| N402HE |  | Lincoln Airport (KLNK) | Lincoln Airport (KLNK) | 2026-07-28 20:49 UTC | 2026-07-28 22:07 UTC | 1h 18m |
| CPA698 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-07-28 17:35 UTC | 2026-07-28 22:06 UTC | 4h 30m |
| ZKLTE | ZKL | Hood Airport (NZMS) | Hood Airport (NZMS) | 2026-07-28 20:31 UTC | 2026-07-28 22:05 UTC | 1h 33m |
| N468WA |  | Kapalua Airport (PHJH) | Kapalua Airport (PHJH) | 2026-07-28 21:39 UTC | 2026-07-28 22:04 UTC | 24m |
| BAW398 | British Airways | London Heathrow Airport (EGLL) | HE42 (HE42) | 2026-07-28 17:54 UTC | 2026-07-28 22:02 UTC | 4h 7m |
| N20H |  | St Paul Downtown Holman Field (KSTP) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-07-28 20:46 UTC | 2026-07-28 22:01 UTC | 1h 15m |
| N48BZ |  | Lawrence J Timmerman Airport (KMWC) | Sss Aerodrome (WI62) | 2026-07-28 21:33 UTC | 2026-07-28 22:00 UTC | 26m |
| R20653 |  | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-07-28 20:06 UTC | 2026-07-28 21:59 UTC | 1h 52m |
| N9454F |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-07-28 21:51 UTC | 2026-07-28 21:54 UTC | 3m |
| PBR680 | PBR | Victoria International Airport (CYYJ) | Boundary Bay Airport (CZBB) | 2026-07-28 21:35 UTC | 2026-07-28 21:52 UTC | 17m |
| N2YV |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-07-28 21:19 UTC | 2026-07-28 21:50 UTC | 30m |
| ZKIAE | ZKI | Waiouru Airport (NZRU) | Waiouru Airport (NZRU) | 2026-07-28 21:27 UTC | 2026-07-28 21:50 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
