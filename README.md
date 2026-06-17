# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--17_19:31:08_UTC-green)

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

**Latest saved flight:** 2026-06-17 19:31:08 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-17 19:31:08 UTC

- **113,524** saved flights
- **39,442** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **113,524** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,383,144.4 tonnes** estimated CO2 emissions
- **80,182,282 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4681 |
| 2 | SkyWest Airlines | 4231 |
| 3 | EJA | 2203 |
| 4 | IndiGo | 2197 |
| 5 | American Airlines | 1789 |
| 6 | Southwest Airlines | 1690 |
| 7 | ENY | 1415 |
| 8 | Delta Air Lines | 1342 |
| 9 | Lufthansa | 1270 |
| 10 | Vueling | 1033 |
| 11 | WIF | 1008 |
| 12 | LATAM Airlines | 1000 |
| 13 | AZU | 951 |
| 14 | AXM | 945 |
| 15 | LXJ | 864 |
| 16 | Swiss International | 810 |
| 17 | All Nippon Airways | 786 |
| 18 | Alaska Airlines | 766 |
| 19 | QLK | 739 |
| 20 | easyJet | 731 |
| 21 | EJU | 716 |
| 22 | Cathay Pacific | 665 |
| 23 | AEE | 636 |
| 24 | VIV | 630 |
| 25 | Air France | 629 |
| 26 | United Airlines | 629 |
| 27 | CXK | 601 |
| 28 | MXY | 601 |
| 29 | AXB | 557 |
| 30 | GLO | 557 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 95760 |
| 2 | 🇪🇸 ES | 7755 |
| 3 | 🇮🇳 IN | 6938 |
| 4 | 🇦🇺 AU | 6722 |
| 5 | 🇧🇷 BR | 6285 |
| 6 | 🇮🇹 IT | 6097 |
| 7 | 🇩🇪 DE | 6073 |
| 8 | 🇨🇦 CA | 5964 |
| 9 | 🇯🇵 JP | 5112 |
| 10 | 🇬🇧 GB | 4904 |
| 11 | 🇫🇷 FR | 4520 |
| 12 | 🇨🇴 CO | 3867 |
| 13 | 🇲🇽 MX | 3355 |
| 14 | 🇬🇷 GR | 3228 |
| 15 | 🇳🇴 NO | 3142 |
| 16 | 🇨🇭 CH | 2903 |
| 17 | 🇲🇾 MY | 2443 |
| 18 | 🇹🇷 TR | 2278 |
| 19 | 🇿🇦 ZA | 1923 |
| 20 | 🇰🇷 KR | 1868 |
| 21 | 🇳🇿 NZ | 1858 |
| 22 | 🇵🇱 PL | 1856 |
| 23 | 🇹🇭 TH | 1843 |
| 24 | 🇵🇭 PH | 1651 |
| 25 | 🇬🇹 GT | 1620 |
| 26 | 🇲🇦 MA | 1245 |
| 27 | 🇲🇴 MO | 1161 |
| 28 | 🇲🇪 ME | 1112 |
| 29 | 🇳🇱 NL | 1103 |
| 30 | 🇭🇷 HR | 988 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2417 |
| 2 | Denver International Airport |  | US | 1921 |
| 3 | Tokyo International Airport |  | JP | 1697 |
| 4 | Indira Gandhi International Airport |  | IN | 1511 |
| 5 | Guaymaral Airport |  | CO | 1431 |
| 6 | Harry Reid International Airport |  | US | 1424 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1395 |
| 8 | Zurich Airport |  | CH | 1277 |
| 9 | La Aurora Airport |  | GT | 1249 |
| 10 | Frankfurt am Main International Airport |  | DE | 1239 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1220 |
| 12 | Macau International Airport |  | MO | 1161 |
| 13 | El Dorado International Airport |  | CO | 1153 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1138 |
| 15 | Chicago O'Hare International Airport |  | US | 1122 |
| 16 | Capua Airport |  | IT | 987 |
| 17 | Madrid Barajas International Airport |  | ES | 981 |
| 18 | Salt Lake City International Airport |  | US | 964 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 956 |
| 20 | Kuala Lumpur International Airport |  | MY | 947 |
| 21 | Charlotte/Douglas International Airport |  | US | 880 |
| 22 | Congonhas Airport |  | BR | 872 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 845 |
| 24 | Charles de Gaulle International Airport |  | FR | 841 |
| 25 | Bengaluru International Airport |  | IN | 840 |
| 26 | Malpensa International Airport |  | IT | 817 |
| 27 | General Edward Lawrence Logan International Airport |  | US | 797 |
| 28 | Ninoy Aquino International Airport |  | PH | 761 |
| 29 | Daniel K Inouye International Airport |  | US | 745 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 745 |
| 31 | Tenerife Norte Airport |  | ES | 741 |
| 32 | Barcelona International Airport |  | ES | 733 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 716 |
| 34 | Amsterdam Airport Schiphol |  | NL | 674 |
| 35 | Don Mueang International Airport |  | TH | 672 |
| 36 | Vitoria/Foronda Airport |  | ES | 672 |
| 37 | Calgary International Airport |  | CA | 667 |
| 38 | Seattle-Tacoma International Airport |  | US | 652 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 650 |
| 40 | Viracopos International Airport |  | BR | 650 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 593 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 411 | 21m | 244 km | 1,730.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 301 | 24m | 225 km | 1,167.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 296 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 284 | 1h 7m | 706 km | 3,457.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 277 | 1h 25m | 910 km | 4,346.8 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 277 | 14m | 114 km | 543.3 t |
| 8 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 270 | 1h 10m | 770 km | 3,586.7 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 228 | 26m | 275 km | 1,080.4 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 225 | 19m | 165 km | 640.0 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 211 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 168 | 20m | 99 km | 287.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 166 | 26m | 215 km | 614.8 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 165 | 22m | 55 km | 156.8 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 164 | 13m | - | - |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 155 | 27m | 152 km | 405.1 t |
| 18 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 153 | 31m | 369 km | 973.9 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 150 | 44m | 452 km | 1,169.0 t |
| 21 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 147 | 44m | 241 km | 610.6 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 147 | 18m | 144 km | 365.7 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 144 | 20m | 250 km | 622.0 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 136 | 1h 1m | 695 km | 1,630.2 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 133 | 1h 43m | 1,423 km | 3,264.0 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 133 | 1h 39m | 1,156 km | 2,653.3 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 127 | 1h 17m | 961 km | 2,105.1 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 127 | 12m | - | - |
| 30 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 126 | 24m | 223 km | 484.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FLC94 | FLC | Ted Stevens Anchorage International Airport (PANC) | Tok Junction Airport (PFTO) | 2026-06-17 17:41 UTC | 2026-06-17 19:31 UTC | 1h 49m |
| N862SL |  | Zamperini Field (KTOA) | Bob Maxwell Memorial Airfield (KOKB) | 2026-06-17 18:43 UTC | 2026-06-17 19:28 UTC | 45m |
| N268Z |  | Palo Alto Airport (KPAO) | Sacramento Executive Airport (KSAC) | 2026-06-17 18:37 UTC | 2026-06-17 19:25 UTC | 47m |
| RNGR773 | RNG | Corpus Christi Nas (Truax Field) Airport (KNGP) | Ingleside Regional Airport (KTFP) | 2026-06-17 18:43 UTC | 2026-06-17 19:20 UTC | 36m |
| N725LV |  | Henderson Executive Airport (KHND) | Henderson Executive Airport (KHND) | 2026-06-17 19:19 UTC | 2026-06-17 19:19 UTC | 0m |
| BOE364 | BOE | Renton Municipal Airport (KRNT) | Franz Ranch Airport (33WA) | 2026-06-17 17:31 UTC | 2026-06-17 19:15 UTC | 1h 44m |
| N3972W |  | Indiana County/Jimmy Stewart Field (KIDI) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-06-17 18:34 UTC | 2026-06-17 19:14 UTC | 40m |
| N622TP |  | Tweed/New Haven Airport (KHVN) | Laguardia Airport (KLGA) | 2026-06-17 18:48 UTC | 2026-06-17 19:12 UTC | 24m |
| PAT079 | PAT | Elmendorf Afb Airport (PAED) | Homer Airport (PAHO) | 2026-06-17 18:05 UTC | 2026-06-17 19:11 UTC | 1h 5m |
| C6018 |  | Kodiak Airport (PADQ) | Kodiak Airport (PADQ) | 2026-06-17 19:05 UTC | 2026-06-17 19:11 UTC | 5m |
| N407DV |  | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-06-17 19:05 UTC | 2026-06-17 19:10 UTC | 5m |
| N96567 |  | Danbury Municipal Airport (KDXR) | Danbury Municipal Airport (KDXR) | 2026-06-17 18:23 UTC | 2026-06-17 19:08 UTC | 44m |
| N930AX |  | Westport Airport (12NK) | Westport Airport (12NK) | 2026-06-17 19:03 UTC | 2026-06-17 19:03 UTC | 0m |
| N727P |  | Bend Municipal Airport (KBDN) | Goering Ranches / Chocheta Estates Airport (50OR) | 2026-06-17 18:33 UTC | 2026-06-17 19:02 UTC | 28m |
| RYR97MQ | Ryanair | Brussels South Charleroi Airport (EBCI) | Manchester Airport (EGCC) | 2026-06-17 17:59 UTC | 2026-06-17 19:01 UTC | 1h 2m |
| APAQUILA | APA | Campo Fontenelle Airport (SBYS) | Comandante Vittorio Bonomi Airport (SJCA) | 2026-06-17 18:50 UTC | 2026-06-17 19:01 UTC | 10m |
| STALK35 | STA | Geary Ranch Airport (CO65) | Central Colorado Regional Airport (KAEJ) | 2026-06-17 18:23 UTC | 2026-06-17 18:58 UTC | 35m |
| N337FB |  | Hudson Valley Regional Airport (KPOU) | Danbury Municipal Airport (KDXR) | 2026-06-17 18:37 UTC | 2026-06-17 18:57 UTC | 20m |
| BB110 |  | St Elmo Airport (K2R5) | Atmore Municipal Airport (K0R1) | 2026-06-17 18:33 UTC | 2026-06-17 18:57 UTC | 24m |
| LXJ374 | LXJ | Harry Reid International Airport (KLAS) | Scottsdale Airport (KSDL) | 2026-06-17 18:07 UTC | 2026-06-17 18:56 UTC | 48m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
