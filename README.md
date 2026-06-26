# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--26_18:09:22_UTC-green)

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

**Latest saved flight:** 2026-06-26 18:09:22 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-26 18:09:22 UTC

- **121,301** saved flights
- **41,668** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **121,301** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,466,063.0 tonnes** estimated CO2 emissions
- **84,989,158 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4971 |
| 2 | SkyWest Airlines | 4481 |
| 3 | EJA | 2340 |
| 4 | IndiGo | 2324 |
| 5 | American Airlines | 1878 |
| 6 | Southwest Airlines | 1810 |
| 7 | ENY | 1511 |
| 8 | Delta Air Lines | 1433 |
| 9 | Lufthansa | 1321 |
| 10 | Vueling | 1084 |
| 11 | LATAM Airlines | 1078 |
| 12 | WIF | 1075 |
| 13 | AZU | 1014 |
| 14 | AXM | 983 |
| 15 | LXJ | 920 |
| 16 | Swiss International | 847 |
| 17 | All Nippon Airways | 825 |
| 18 | Alaska Airlines | 798 |
| 19 | easyJet | 780 |
| 20 | QLK | 774 |
| 21 | EJU | 763 |
| 22 | Cathay Pacific | 678 |
| 23 | AEE | 672 |
| 24 | Air France | 666 |
| 25 | VIV | 662 |
| 26 | United Airlines | 659 |
| 27 | CXK | 649 |
| 28 | MXY | 635 |
| 29 | JetBlue | 604 |
| 30 | AXB | 602 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 102931 |
| 2 | 🇪🇸 ES | 8216 |
| 3 | 🇮🇳 IN | 7304 |
| 4 | 🇦🇺 AU | 7126 |
| 5 | 🇧🇷 BR | 6677 |
| 6 | 🇩🇪 DE | 6473 |
| 7 | 🇮🇹 IT | 6454 |
| 8 | 🇨🇦 CA | 6368 |
| 9 | 🇯🇵 JP | 5389 |
| 10 | 🇬🇧 GB | 5329 |
| 11 | 🇫🇷 FR | 4820 |
| 12 | 🇨🇴 CO | 4024 |
| 13 | 🇲🇽 MX | 3528 |
| 14 | 🇬🇷 GR | 3466 |
| 15 | 🇳🇴 NO | 3350 |
| 16 | 🇨🇭 CH | 3118 |
| 17 | 🇲🇾 MY | 2549 |
| 18 | 🇹🇷 TR | 2508 |
| 19 | 🇿🇦 ZA | 2027 |
| 20 | 🇵🇱 PL | 1993 |
| 21 | 🇳🇿 NZ | 1960 |
| 22 | 🇹🇭 TH | 1921 |
| 23 | 🇰🇷 KR | 1917 |
| 24 | 🇵🇭 PH | 1740 |
| 25 | 🇬🇹 GT | 1687 |
| 26 | 🇲🇦 MA | 1304 |
| 27 | 🇲🇪 ME | 1210 |
| 28 | 🇲🇴 MO | 1174 |
| 29 | 🇳🇱 NL | 1156 |
| 30 | 🇭🇷 HR | 1051 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2543 |
| 2 | Denver International Airport |  | US | 2037 |
| 3 | Tokyo International Airport |  | JP | 1784 |
| 4 | Indira Gandhi International Airport |  | IN | 1609 |
| 5 | Guaymaral Airport |  | CO | 1514 |
| 6 | Harry Reid International Airport |  | US | 1507 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1468 |
| 8 | Zurich Airport |  | CH | 1344 |
| 9 | La Aurora Airport |  | GT | 1303 |
| 10 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1287 |
| 11 | Frankfurt am Main International Airport |  | DE | 1275 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1196 |
| 13 | Chicago O'Hare International Airport |  | US | 1181 |
| 14 | Macau International Airport |  | MO | 1174 |
| 15 | El Dorado International Airport |  | CO | 1171 |
| 16 | Salt Lake City International Airport |  | US | 1054 |
| 17 | Capua Airport |  | IT | 1038 |
| 18 | Madrid Barajas International Airport |  | ES | 1017 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1011 |
| 20 | Kuala Lumpur International Airport |  | MY | 988 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 949 |
| 22 | Congonhas Airport |  | BR | 935 |
| 23 | Charlotte/Douglas International Airport |  | US | 914 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 900 |
| 25 | Charles de Gaulle International Airport |  | FR | 891 |
| 26 | Bengaluru International Airport |  | IN | 877 |
| 27 | Malpensa International Airport |  | IT | 846 |
| 28 | Ninoy Aquino International Airport |  | PH | 806 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 789 |
| 30 | Daniel K Inouye International Airport |  | US | 782 |
| 31 | Barcelona International Airport |  | ES | 762 |
| 32 | Tenerife Norte Airport |  | ES | 762 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 743 |
| 34 | Calgary International Airport |  | CA | 708 |
| 35 | Vitoria/Foronda Airport |  | ES | 707 |
| 36 | Amsterdam Airport Schiphol |  | NL | 699 |
| 37 | Scottsdale Airport |  | US | 696 |
| 38 | Norman Y Mineta San Jose International Airport |  | US | 695 |
| 39 | Seattle-Tacoma International Airport |  | US | 695 |
| 40 | Don Mueang International Airport |  | TH | 694 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 631 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 442 | 21m | 244 km | 1,861.1 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 318 | 24m | 225 km | 1,233.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 309 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 293 | 1h 10m | 770 km | 3,892.3 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 292 | 1h 25m | 910 km | 4,582.2 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 238 | 26m | 275 km | 1,127.8 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 225 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 178 | 22m | 55 km | 169.2 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 175 | 26m | 215 km | 648.1 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 174 | 20m | 99 km | 298.0 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 170 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 166 | 44m | 241 km | 689.5 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 164 | 27m | 152 km | 428.6 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 156 | 31m | 369 km | 993.0 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 154 | 44m | 452 km | 1,200.2 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 153 | 1h 44m | 1,423 km | 3,754.9 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 151 | 18m | 144 km | 375.6 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 150 | 20m | 250 km | 647.9 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 142 | 1h 38m | 1,156 km | 2,832.8 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 141 | 1h 1m | 695 km | 1,690.2 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 137 | 1h 17m | 961 km | 2,270.8 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 136 | 13m | - | - |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 135 | 20m | 147 km | 341.6 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 133 | 29m | 49 km | 112.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N4414X |  | Wings Field (KLOM) | Pottstown Municipal Airport (KN47) | 2026-06-26 17:35 UTC | 2026-06-26 18:09 UTC | 33m |
| N9731F |  | Witham Field (KSUA) | North Palm Beach County General Aviation Airport (KF45) | 2026-06-26 17:22 UTC | 2026-06-26 18:07 UTC | 45m |
| N978AP |  | Gillespie Field (KSEE) | Meadows Field (KBFL) | 2026-06-26 16:07 UTC | 2026-06-26 18:07 UTC | 1h 59m |
| BRG621 | BRG | Shungnak Airport (PAGH) | Ambler Airport (PAFM) | 2026-06-26 17:54 UTC | 2026-06-26 18:04 UTC | 10m |
| GLOCK11 | GLO | Four Square Ranch Airport (3TA0) | Four Square Ranch Airport (3TA0) | 2026-06-26 17:53 UTC | 2026-06-26 18:03 UTC | 10m |
| N690SG |  | Wendover Airport (KENV) | UT99 (UT99) | 2026-06-26 17:36 UTC | 2026-06-26 18:02 UTC | 26m |
| AUB1340 | AUB | Auburn University Regional Airport (KAUO) | Columbus Airport (KCSG) | 2026-06-26 17:46 UTC | 2026-06-26 18:00 UTC | 13m |
| N16895 |  | Easterwood Field (KCLL) | Corpora Airport (1TE5) | 2026-06-26 17:47 UTC | 2026-06-26 18:00 UTC | 12m |
| N538SV |  | Los Alamos Airport (KLAM) | 50NM (50NM) | 2026-06-26 17:43 UTC | 2026-06-26 17:59 UTC | 15m |
| N631HB |  | Mcknight Airport (5OI8) | Knox County Airport (K4I3) | 2026-06-26 17:40 UTC | 2026-06-26 17:57 UTC | 17m |
| N79975 |  | Princeton Airport (K39N) | Lehigh Valley International Airport (KABE) | 2026-06-26 17:18 UTC | 2026-06-26 17:52 UTC | 33m |
| N68PA |  | La Mole Airport (LFTZ) | Nice-Cote d'Azur Airport (LFMN) | 2026-06-26 17:34 UTC | 2026-06-26 17:49 UTC | 15m |
| VAR851 | VAR | Phoenix Goodyear Airport (KGYR) | Buckeye Municipal Airport (KBXK) | 2026-06-26 17:32 UTC | 2026-06-26 17:47 UTC | 14m |
| N1929Y |  | Gillespie Field (KSEE) | K36U (K36U) | 2026-06-26 16:33 UTC | 2026-06-26 17:47 UTC | 1h 14m |
| N237TH |  | Montgomery-Gibbs Executive Airport (KMYF) | Bob Maxwell Memorial Airfield (KOKB) | 2026-06-26 17:06 UTC | 2026-06-26 17:45 UTC | 39m |
| N6046G |  | Marana Regional Airport (KAVQ) | Scottsdale Airport (KSDL) | 2026-06-26 16:58 UTC | 2026-06-26 17:44 UTC | 45m |
| N5396E |  | Montgomery-Gibbs Executive Airport (KMYF) | Ramona Airport (KRNM) | 2026-06-26 17:03 UTC | 2026-06-26 17:43 UTC | 40m |
| N331PR |  | Eagle Ridge Airport (SC24) | Twin County Airport (KHLX) | 2026-06-26 17:13 UTC | 2026-06-26 17:43 UTC | 30m |
| N103UV |  | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-06-26 16:46 UTC | 2026-06-26 17:43 UTC | 56m |
| ARCAS15 | ARC | Danaher Airport (7TX0) | TX20 (TX20) | 2026-06-26 17:19 UTC | 2026-06-26 17:42 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
