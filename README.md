# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--08_11:18:53_UTC-green)

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

**Latest saved flight:** 2026-06-08 11:18:53 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-08 11:18:53 UTC

- **105,877** saved flights
- **37,223** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **105,877** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,295,529.6 tonnes** estimated CO2 emissions
- **75,103,167 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4371 |
| 2 | SkyWest Airlines | 3979 |
| 3 | IndiGo | 2107 |
| 4 | EJA | 2023 |
| 5 | American Airlines | 1696 |
| 6 | Southwest Airlines | 1597 |
| 7 | ENY | 1327 |
| 8 | Delta Air Lines | 1255 |
| 9 | Lufthansa | 1215 |
| 10 | Vueling | 973 |
| 11 | LATAM Airlines | 935 |
| 12 | WIF | 928 |
| 13 | AXM | 910 |
| 14 | AZU | 853 |
| 15 | LXJ | 798 |
| 16 | Swiss International | 768 |
| 17 | All Nippon Airways | 741 |
| 18 | Alaska Airlines | 732 |
| 19 | QLK | 710 |
| 20 | easyJet | 687 |
| 21 | EJU | 674 |
| 22 | Cathay Pacific | 633 |
| 23 | AEE | 611 |
| 24 | VIV | 605 |
| 25 | Air France | 604 |
| 26 | United Airlines | 586 |
| 27 | MXY | 578 |
| 28 | CXK | 557 |
| 29 | Japan Airlines | 526 |
| 30 | AXB | 517 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 88942 |
| 2 | 🇪🇸 ES | 7286 |
| 3 | 🇮🇳 IN | 6644 |
| 4 | 🇦🇺 AU | 6387 |
| 5 | 🇧🇷 BR | 5792 |
| 6 | 🇩🇪 DE | 5693 |
| 7 | 🇮🇹 IT | 5670 |
| 8 | 🇨🇦 CA | 5504 |
| 9 | 🇯🇵 JP | 4874 |
| 10 | 🇬🇧 GB | 4484 |
| 11 | 🇫🇷 FR | 4210 |
| 12 | 🇨🇴 CO | 3645 |
| 13 | 🇲🇽 MX | 3161 |
| 14 | 🇬🇷 GR | 3012 |
| 15 | 🇳🇴 NO | 2932 |
| 16 | 🇨🇭 CH | 2706 |
| 17 | 🇲🇾 MY | 2334 |
| 18 | 🇹🇷 TR | 2042 |
| 19 | 🇿🇦 ZA | 1832 |
| 20 | 🇰🇷 KR | 1773 |
| 21 | 🇳🇿 NZ | 1766 |
| 22 | 🇹🇭 TH | 1759 |
| 23 | 🇵🇱 PL | 1726 |
| 24 | 🇵🇭 PH | 1565 |
| 25 | 🇬🇹 GT | 1529 |
| 26 | 🇲🇦 MA | 1171 |
| 27 | 🇲🇴 MO | 1107 |
| 28 | 🇳🇱 NL | 1037 |
| 29 | 🇲🇪 ME | 1020 |
| 30 | 🇭🇷 HR | 924 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2296 |
| 2 | Denver International Airport |  | US | 1810 |
| 3 | Tokyo International Airport |  | JP | 1613 |
| 4 | Indira Gandhi International Airport |  | IN | 1444 |
| 5 | Harry Reid International Airport |  | US | 1355 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1336 |
| 7 | Guaymaral Airport |  | CO | 1327 |
| 8 | Frankfurt am Main International Airport |  | DE | 1204 |
| 9 | Zurich Airport |  | CH | 1199 |
| 10 | La Aurora Airport |  | GT | 1177 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1140 |
| 12 | El Dorado International Airport |  | CO | 1112 |
| 13 | Macau International Airport |  | MO | 1107 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1066 |
| 15 | Chicago O'Hare International Airport |  | US | 1063 |
| 16 | Madrid Barajas International Airport |  | ES | 926 |
| 17 | Kuala Lumpur International Airport |  | MY | 915 |
| 18 | Salt Lake City International Airport |  | US | 905 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 905 |
| 20 | Capua Airport |  | IT | 899 |
| 21 | Charlotte/Douglas International Airport |  | US | 822 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 814 |
| 23 | Charles de Gaulle International Airport |  | FR | 804 |
| 24 | Congonhas Airport |  | BR | 804 |
| 25 | Malpensa International Airport |  | IT | 794 |
| 26 | Bengaluru International Airport |  | IN | 793 |
| 27 | Daniel K Inouye International Airport |  | US | 721 |
| 28 | Tenerife Norte Airport |  | ES | 718 |
| 29 | Ninoy Aquino International Airport |  | PH | 717 |
| 30 | Barcelona International Airport |  | ES | 694 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 683 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 682 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 680 |
| 34 | Don Mueang International Airport |  | TH | 643 |
| 35 | Amsterdam Airport Schiphol |  | NL | 642 |
| 36 | Vitoria/Foronda Airport |  | ES | 634 |
| 37 | Calgary International Airport |  | CA | 625 |
| 38 | Seattle-Tacoma International Airport |  | US | 616 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 606 |
| 40 | Netaji Subhash Chandra Bose International Airport |  | IN | 605 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 548 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 389 | 21m | 244 km | 1,638.0 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 284 | 24m | 225 km | 1,101.8 t |
| 4 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 281 | 1h 7m | 706 km | 3,421.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 276 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 267 | 14m | 114 km | 523.7 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 260 | 1h 25m | 910 km | 4,080.0 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 259 | 28m | 304 km | 1,357.7 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 245 | 1h 10m | 770 km | 3,254.6 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 220 | 19m | 165 km | 625.8 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 212 | 26m | 275 km | 1,004.6 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 204 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 161 | 20m | 99 km | 275.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 155 | 27m | 215 km | 574.1 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 155 | 22m | 55 km | 147.3 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 150 | 14m | 154 km | 397.4 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 147 | 31m | 369 km | 935.7 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 146 | 27m | 152 km | 381.6 t |
| 19 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 145 | 44m | 452 km | 1,130.1 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 142 | 13m | - | - |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 139 | 18m | 144 km | 345.8 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 130 | 1h 1m | 695 km | 1,558.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 123 | 1h 43m | 1,423 km | 3,018.6 t |
| 27 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 123 | 44m | 241 km | 510.9 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 121 | 1h 52m | 1,304 km | 2,722.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 119 | 1h 18m | 961 km | 1,972.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ETP08 | ETP | Old Sarum Airfield (EGLS) | Old Sarum Airfield (EGLS) | 2026-06-08 10:56 UTC | 2026-06-08 11:18 UTC | 22m |
| UAE719 | Emirates | Jomo Kenyatta International Airport (HKJK) | Jomo Kenyatta International Airport (HKJK) | 2026-06-08 11:12 UTC | 2026-06-08 11:18 UTC | 5m |
| DHFJB | DHF | Reichelsheim Airport (EDFB) | Reichelsheim Airport (EDFB) | 2026-06-08 10:57 UTC | 2026-06-08 11:15 UTC | 17m |
| BASIC33 | BAS | Pardubice Airport (LKPD) | Pardubice Airport (LKPD) | 2026-06-08 10:27 UTC | 2026-06-08 11:14 UTC | 47m |
| N470LP |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-06-08 10:56 UTC | 2026-06-08 11:13 UTC | 17m |
| JMA8665 | JMA | Nairobi Wilson Airport (HKNW) | Nairobi Wilson Airport (HKNW) | 2026-06-08 11:09 UTC | 2026-06-08 11:09 UTC | 0m |
| FHLID | FHL | Rathcoole Aerodrome (EIRT) | Kerry Airport (EIKY) | 2026-06-08 09:40 UTC | 2026-06-08 11:07 UTC | 1h 27m |
| N80298 |  | Miami Executive Airport (KTMB) | Miami Homestead General Aviation Airport (KX51) | 2026-06-08 10:49 UTC | 2026-06-08 11:05 UTC | 16m |
| N820DL |  | Piedmont Triad International Airport (KGSO) | NC87 (NC87) | 2026-06-08 10:19 UTC | 2026-06-08 10:55 UTC | 35m |
| WIF77P | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-06-08 10:07 UTC | 2026-06-08 10:53 UTC | 46m |
| MPC003 | MPC | Farnborough Airport (EGLF) | Tivat Airport (LYTV) | 2026-06-08 08:38 UTC | 2026-06-08 10:53 UTC | 2h 14m |
| N127GA |  | Flying Cloud Airport (KFCM) | SD66 (SD66) | 2026-06-08 09:15 UTC | 2026-06-08 10:50 UTC | 1h 34m |
| PRFJV | PRF | Jundiai Airport (SBJD) | Lencois Paulista Airport (SDLP) | 2026-06-08 10:09 UTC | 2026-06-08 10:45 UTC | 36m |
| IGO295C | IndiGo | Indira Gandhi International Airport (VIDP) | Sidhi Airport (VA1F) | 2026-06-08 09:47 UTC | 2026-06-08 10:39 UTC | 52m |
| IBB97FU | IBB | Tenerife Norte Airport (GCXO) | La Morgal Airport (LEMR) | 2026-06-08 08:13 UTC | 2026-06-08 10:36 UTC | 2h 22m |
| ZAM19 | ZAM | Al Udeid Air Base (OTBH) | Al Udeid Air Base (OTBH) | 2026-06-08 10:31 UTC | 2026-06-08 10:35 UTC | 4m |
| IGO411Y | IndiGo | Juhu Aerodrome (VAJJ) | Baglung Airport (VNBL) | 2026-06-08 08:54 UTC | 2026-06-08 10:33 UTC | 1h 38m |
| RYR5CD | Ryanair | Palma De Mallorca Airport (LEPA) | Liverpool John Lennon Airport (EGGP) | 2026-06-08 08:17 UTC | 2026-06-08 10:33 UTC | 2h 15m |
| RYR84TT | Ryanair | Barcelona International Airport (LEBL) | Napoli / Capodichino International Airport (LIRN) | 2026-06-08 09:09 UTC | 2026-06-08 10:32 UTC | 1h 22m |
| AIQ3256 | AIQ | Don Mueang International Airport (VTBD) | Khorat Airport (VTUN) | 2026-06-08 10:05 UTC | 2026-06-08 10:32 UTC | 27m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
