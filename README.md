# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--03_18:04:28_UTC-green)

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

**Latest saved flight:** 2026-07-03 18:04:28 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-03 18:04:28 UTC

- **127,767** saved flights
- **43,584** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **127,767** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,541,315.3 tonnes** estimated CO2 emissions
- **89,351,612 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5183 |
| 2 | SkyWest Airlines | 4720 |
| 3 | EJA | 2508 |
| 4 | IndiGo | 2413 |
| 5 | American Airlines | 1962 |
| 6 | Southwest Airlines | 1917 |
| 7 | ENY | 1601 |
| 8 | Delta Air Lines | 1522 |
| 9 | Lufthansa | 1354 |
| 10 | LATAM Airlines | 1162 |
| 11 | Vueling | 1130 |
| 12 | WIF | 1125 |
| 13 | AZU | 1078 |
| 14 | AXM | 1002 |
| 15 | LXJ | 992 |
| 16 | Swiss International | 886 |
| 17 | All Nippon Airways | 853 |
| 18 | Alaska Airlines | 827 |
| 19 | easyJet | 815 |
| 20 | QLK | 803 |
| 21 | EJU | 791 |
| 22 | Cathay Pacific | 708 |
| 23 | VIV | 701 |
| 24 | AEE | 700 |
| 25 | Air France | 698 |
| 26 | CXK | 687 |
| 27 | United Airlines | 676 |
| 28 | MXY | 665 |
| 29 | JetBlue | 654 |
| 30 | GLO | 645 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 109293 |
| 2 | 🇪🇸 ES | 8506 |
| 3 | 🇮🇳 IN | 7560 |
| 4 | 🇦🇺 AU | 7449 |
| 5 | 🇧🇷 BR | 7143 |
| 6 | 🇩🇪 DE | 6736 |
| 7 | 🇨🇦 CA | 6725 |
| 8 | 🇮🇹 IT | 6705 |
| 9 | 🇬🇧 GB | 5642 |
| 10 | 🇯🇵 JP | 5567 |
| 11 | 🇫🇷 FR | 5063 |
| 12 | 🇨🇴 CO | 4064 |
| 13 | 🇲🇽 MX | 3717 |
| 14 | 🇬🇷 GR | 3635 |
| 15 | 🇳🇴 NO | 3494 |
| 16 | 🇨🇭 CH | 3248 |
| 17 | 🇹🇷 TR | 2726 |
| 18 | 🇲🇾 MY | 2597 |
| 19 | 🇿🇦 ZA | 2124 |
| 20 | 🇵🇱 PL | 2088 |
| 21 | 🇳🇿 NZ | 2059 |
| 22 | 🇹🇭 TH | 1990 |
| 23 | 🇰🇷 KR | 1958 |
| 24 | 🇵🇭 PH | 1804 |
| 25 | 🇬🇹 GT | 1751 |
| 26 | 🇲🇦 MA | 1371 |
| 27 | 🇲🇪 ME | 1263 |
| 28 | 🇳🇱 NL | 1204 |
| 29 | 🇲🇴 MO | 1184 |
| 30 | 🇧🇸 BS | 1104 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2666 |
| 2 | Denver International Airport |  | US | 2152 |
| 3 | Tokyo International Airport |  | JP | 1835 |
| 4 | Indira Gandhi International Airport |  | IN | 1664 |
| 5 | Harry Reid International Airport |  | US | 1595 |
| 6 | Guaymaral Airport |  | CO | 1551 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1516 |
| 8 | Zurich Airport |  | CH | 1402 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1362 |
| 10 | La Aurora Airport |  | GT | 1355 |
| 11 | Frankfurt am Main International Airport |  | DE | 1312 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1246 |
| 13 | Chicago O'Hare International Airport |  | US | 1235 |
| 14 | Macau International Airport |  | MO | 1184 |
| 15 | El Dorado International Airport |  | CO | 1172 |
| 16 | Salt Lake City International Airport |  | US | 1128 |
| 17 | Capua Airport |  | IT | 1067 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1057 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1053 |
| 20 | Madrid Barajas International Airport |  | ES | 1046 |
| 21 | Kuala Lumpur International Airport |  | MY | 1010 |
| 22 | Congonhas Airport |  | BR | 1004 |
| 23 | Charlotte/Douglas International Airport |  | US | 961 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 935 |
| 25 | Charles de Gaulle International Airport |  | FR | 930 |
| 26 | Bengaluru International Airport |  | IN | 916 |
| 27 | Malpensa International Airport |  | IT | 872 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 857 |
| 29 | Ninoy Aquino International Airport |  | PH | 836 |
| 30 | Daniel K Inouye International Airport |  | US | 809 |
| 31 | Barcelona International Airport |  | ES | 795 |
| 32 | Tenerife Norte Airport |  | ES | 780 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 776 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 749 |
| 35 | Calgary International Airport |  | CA | 746 |
| 36 | Scottsdale Airport |  | US | 739 |
| 37 | Seattle-Tacoma International Airport |  | US | 737 |
| 38 | Vitoria/Foronda Airport |  | ES | 737 |
| 39 | Viracopos International Airport |  | BR | 727 |
| 40 | Amsterdam Airport Schiphol |  | NL | 726 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 648 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 464 | 21m | 244 km | 1,953.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 328 | 24m | 225 km | 1,272.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 322 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 309 | 1h 10m | 770 km | 4,104.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 244 | 26m | 275 km | 1,156.2 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 236 | 31m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 188 | 22m | 55 km | 178.7 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 181 | 26m | 215 km | 670.3 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 178 | 44m | 241 km | 739.4 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 177 | 13m | - | - |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 177 | 20m | 99 km | 303.2 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 172 | 27m | 152 km | 449.5 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 166 | 1h 45m | 1,423 km | 4,073.9 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 162 | 31m | 369 km | 1,031.2 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 157 | 20m | 250 km | 678.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 157 | 18m | 144 km | 390.5 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 156 | 44m | 452 km | 1,215.8 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 25 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 153 | 30m | 49 km | 129.3 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 150 | 1h 1m | 695 km | 1,798.1 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 148 | 1h 17m | 961 km | 2,453.2 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 147 | 1h 38m | 1,156 km | 2,932.6 t |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 146 | 54m | 136 km | 342.3 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 141 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| PNC0801 | PNC | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-07-03 17:51 UTC | 2026-07-03 18:04 UTC | 12m |
| LIFELN5 | LIF | West Pueblo Airport (7CO8) | Fremont County Airport (K1V6) | 2026-07-03 17:50 UTC | 2026-07-03 18:01 UTC | 10m |
| VPCVI | VPC | Norman Y Mineta San Jose International Airport (KSJC) | Meadows Field (KBFL) | 2026-07-03 17:20 UTC | 2026-07-03 17:59 UTC | 39m |
| N343KT |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-07-03 17:12 UTC | 2026-07-03 17:49 UTC | 36m |
| N506FA |  | Paxton Airport (K1C1) | Schertz Field (9IS2) | 2026-07-03 17:36 UTC | 2026-07-03 17:48 UTC | 12m |
| N4593Y |  | Boulder Municipal Airport (KBDU) | Boulder Municipal Airport (KBDU) | 2026-07-03 16:44 UTC | 2026-07-03 17:47 UTC | 1h 3m |
| N168Y |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-07-03 17:33 UTC | 2026-07-03 17:45 UTC | 11m |
| N810SC |  | North Las Vegas Airport (KVGT) | Sky Ranch Airport (K3L2) | 2026-07-03 17:34 UTC | 2026-07-03 17:45 UTC | 11m |
| N80945 |  | Mc Kinley Country Airport (81AK) | Helio Airport (2AK7) | 2026-07-03 17:32 UTC | 2026-07-03 17:45 UTC | 12m |
| DFKJM | DFK | Bologna / Borgo Panigale Airport (LIPE) | Hamburg Airport (EDDH) | 2026-07-03 15:03 UTC | 2026-07-03 17:42 UTC | 2h 39m |
| PPNBB | PPN | Congonhas Airport (SBSP) | Araxa Airport (SBAX) | 2026-07-03 16:56 UTC | 2026-07-03 17:39 UTC | 42m |
| N106TJ |  | Malad City Airport (KMLD) | Logan-Cache Airport (KLGU) | 2026-07-03 17:07 UTC | 2026-07-03 17:38 UTC | 30m |
| N639PC |  | H & J Strip (0NC1) | Montréal (Mirabel) Airport (CYMX) | 2026-07-03 13:07 UTC | 2026-07-03 17:31 UTC | 4h 24m |
| N815SS |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-07-03 16:35 UTC | 2026-07-03 17:29 UTC | 54m |
| FHNTA | FHN | Saint-Etienne-Boutheon Airport (LFMH) | La Mole Airport (LFTZ) | 2026-07-03 16:24 UTC | 2026-07-03 17:28 UTC | 1h 4m |
| SJN3 | SJN | Bellingham International Airport (KBLI) | Friday Harbor Airport (KFHR) | 2026-07-03 17:09 UTC | 2026-07-03 17:24 UTC | 14m |
| RYR9AH | Ryanair | Birmingham International Airport (EGBB) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-07-03 15:25 UTC | 2026-07-03 17:22 UTC | 1h 57m |
| SWR77M | Swiss International | Zurich Airport (LSZH) | Graz Airport (LOWG) | 2026-07-03 16:35 UTC | 2026-07-03 17:22 UTC | 47m |
| N559SH |  | Gold King Creek Airport (PAAN) | Healy River Airport (PAHV) | 2026-07-03 16:59 UTC | 2026-07-03 17:21 UTC | 21m |
| N666WC |  | Madera Municipal Airport (KMAE) | Mammoth Yosemite Airport (KMMH) | 2026-07-03 16:57 UTC | 2026-07-03 17:18 UTC | 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
