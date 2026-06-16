# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--16_15:18:00_UTC-green)

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

**Latest saved flight:** 2026-06-16 15:18:00 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-16 15:18:00 UTC

- **112,116** saved flights
- **39,047** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **112,116** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,369,712.5 tonnes** estimated CO2 emissions
- **79,403,624 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4620 |
| 2 | SkyWest Airlines | 4187 |
| 3 | IndiGo | 2187 |
| 4 | EJA | 2169 |
| 5 | American Airlines | 1768 |
| 6 | Southwest Airlines | 1673 |
| 7 | ENY | 1399 |
| 8 | Delta Air Lines | 1328 |
| 9 | Lufthansa | 1263 |
| 10 | Vueling | 1028 |
| 11 | WIF | 992 |
| 12 | LATAM Airlines | 987 |
| 13 | AXM | 939 |
| 14 | AZU | 929 |
| 15 | LXJ | 854 |
| 16 | Swiss International | 803 |
| 17 | All Nippon Airways | 780 |
| 18 | Alaska Airlines | 758 |
| 19 | QLK | 734 |
| 20 | easyJet | 723 |
| 21 | EJU | 712 |
| 22 | Cathay Pacific | 664 |
| 23 | AEE | 632 |
| 24 | Air France | 626 |
| 25 | United Airlines | 625 |
| 26 | VIV | 624 |
| 27 | MXY | 598 |
| 28 | CXK | 590 |
| 29 | AXB | 552 |
| 30 | GLO | 548 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 94407 |
| 2 | 🇪🇸 ES | 7690 |
| 3 | 🇮🇳 IN | 6901 |
| 4 | 🇦🇺 AU | 6654 |
| 5 | 🇧🇷 BR | 6184 |
| 6 | 🇮🇹 IT | 6023 |
| 7 | 🇩🇪 DE | 5999 |
| 8 | 🇨🇦 CA | 5891 |
| 9 | 🇯🇵 JP | 5063 |
| 10 | 🇬🇧 GB | 4834 |
| 11 | 🇫🇷 FR | 4466 |
| 12 | 🇨🇴 CO | 3798 |
| 13 | 🇲🇽 MX | 3313 |
| 14 | 🇬🇷 GR | 3187 |
| 15 | 🇳🇴 NO | 3100 |
| 16 | 🇨🇭 CH | 2875 |
| 17 | 🇲🇾 MY | 2429 |
| 18 | 🇹🇷 TR | 2238 |
| 19 | 🇿🇦 ZA | 1909 |
| 20 | 🇰🇷 KR | 1853 |
| 21 | 🇹🇭 TH | 1840 |
| 22 | 🇳🇿 NZ | 1840 |
| 23 | 🇵🇱 PL | 1833 |
| 24 | 🇵🇭 PH | 1633 |
| 25 | 🇬🇹 GT | 1602 |
| 26 | 🇲🇦 MA | 1233 |
| 27 | 🇲🇴 MO | 1159 |
| 28 | 🇲🇪 ME | 1097 |
| 29 | 🇳🇱 NL | 1090 |
| 30 | 🇭🇷 HR | 974 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2391 |
| 2 | Denver International Airport |  | US | 1900 |
| 3 | Tokyo International Airport |  | JP | 1679 |
| 4 | Indira Gandhi International Airport |  | IN | 1502 |
| 5 | Guaymaral Airport |  | CO | 1409 |
| 6 | Harry Reid International Airport |  | US | 1407 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1386 |
| 8 | Zurich Airport |  | CH | 1262 |
| 9 | La Aurora Airport |  | GT | 1233 |
| 10 | Frankfurt am Main International Airport |  | DE | 1232 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1203 |
| 12 | Macau International Airport |  | MO | 1159 |
| 13 | El Dorado International Airport |  | CO | 1144 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1121 |
| 15 | Chicago O'Hare International Airport |  | US | 1116 |
| 16 | Madrid Barajas International Airport |  | ES | 975 |
| 17 | Capua Airport |  | IT | 973 |
| 18 | Salt Lake City International Airport |  | US | 949 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 942 |
| 20 | Kuala Lumpur International Airport |  | MY | 942 |
| 21 | Charlotte/Douglas International Airport |  | US | 862 |
| 22 | Congonhas Airport |  | BR | 861 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 840 |
| 24 | Charles de Gaulle International Airport |  | FR | 838 |
| 25 | Bengaluru International Airport |  | IN | 835 |
| 26 | Malpensa International Airport |  | IT | 812 |
| 27 | General Edward Lawrence Logan International Airport |  | US | 764 |
| 28 | Ninoy Aquino International Airport |  | PH | 754 |
| 29 | Daniel K Inouye International Airport |  | US | 741 |
| 30 | Tenerife Norte Airport |  | ES | 736 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 732 |
| 32 | Barcelona International Airport |  | ES | 731 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 711 |
| 34 | Don Mueang International Airport |  | TH | 670 |
| 35 | Amsterdam Airport Schiphol |  | NL | 670 |
| 36 | Vitoria/Foronda Airport |  | ES | 665 |
| 37 | Calgary International Airport |  | CA | 660 |
| 38 | Seattle-Tacoma International Airport |  | US | 646 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 645 |
| 40 | Viracopos International Airport |  | BR | 635 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 584 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 408 | 21m | 244 km | 1,718.0 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 298 | 24m | 225 km | 1,156.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 291 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 284 | 1h 7m | 706 km | 3,457.7 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 275 | 14m | 114 km | 539.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 272 | 1h 25m | 910 km | 4,268.3 t |
| 8 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 264 | 1h 10m | 770 km | 3,507.0 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 225 | 26m | 275 km | 1,066.2 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 225 | 19m | 165 km | 640.0 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 209 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 167 | 20m | 99 km | 286.1 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 163 | 27m | 215 km | 603.7 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 163 | 22m | 55 km | 154.9 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 162 | 13m | - | - |
| 17 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 153 | 27m | 152 km | 399.8 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 152 | 31m | 369 km | 967.5 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 149 | 44m | 452 km | 1,161.2 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 146 | 18m | 144 km | 363.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 144 | 20m | 250 km | 622.0 t |
| 23 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 143 | 44m | 241 km | 594.0 t |
| 24 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 134 | 1h 1m | 695 km | 1,606.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 133 | 1h 39m | 1,156 km | 2,653.3 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 132 | 1h 43m | 1,423 km | 3,239.5 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 127 | 12m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 125 | 1h 17m | 961 km | 2,071.9 t |
| 30 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 124 | 24m | 223 km | 477.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CONGO65 | CON | Usaf Academy Davis Airfield (KAFF) | Usaf Academy Davis Airfield (KAFF) | 2026-06-16 14:11 UTC | 2026-06-16 15:18 UTC | 1h 6m |
| ARCAS41 | ARC | 4TA5 (4TA5) | TX20 (TX20) | 2026-06-16 14:57 UTC | 2026-06-16 15:12 UTC | 14m |
| DEFTD | DEF | Aschaffenburg Airport (EDFC) | Aschaffenburg Airport (EDFC) | 2026-06-16 14:37 UTC | 2026-06-16 15:11 UTC | 34m |
| ULC7P | ULC | Luxembourg-Findel International Airport (ELLX) | Zurich Airport (LSZH) | 2026-06-16 14:35 UTC | 2026-06-16 15:08 UTC | 33m |
| N359AL |  | Hickory Regional Airport (KHKY) | Lincoln County Regional Airport (KIPJ) | 2026-06-16 14:51 UTC | 2026-06-16 15:05 UTC | 13m |
| CONGO63 | CON | Usaf Academy Davis Airfield (KAFF) | Usaf Academy Davis Airfield (KAFF) | 2026-06-16 14:31 UTC | 2026-06-16 15:05 UTC | 34m |
| AIB52IL | AIB | Toulouse-Blagnac Airport (LFBO) | Toulouse-Blagnac Airport (LFBO) | 2026-06-16 14:52 UTC | 2026-06-16 15:05 UTC | 12m |
| CGVJE | CGV | Lachute Airport (CSE4) | Lachute Airport (CSE4) | 2026-06-16 14:36 UTC | 2026-06-16 15:04 UTC | 27m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-06-16 13:58 UTC | 2026-06-16 15:03 UTC | 1h 5m |
| IAM1490 | IAM | Pratica Di Mare Airport (LIRE) | Sarajevo International Airport (LQSA) | 2026-06-16 13:46 UTC | 2026-06-16 15:02 UTC | 1h 15m |
| N887DC |  | Modesto City-County-Harry Sham Field (KMOD) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-06-16 14:39 UTC | 2026-06-16 14:58 UTC | 19m |
| N1910R |  | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-06-16 14:41 UTC | 2026-06-16 14:57 UTC | 15m |
| N195PC |  | Hampton Roads Executive Airport (KPVG) | Hampton Roads Executive Airport (KPVG) | 2026-06-16 14:27 UTC | 2026-06-16 14:57 UTC | 30m |
| TGMSD | TGM | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-06-16 14:37 UTC | 2026-06-16 14:55 UTC | 17m |
| N1022G |  | Mc Clellan Airfield (KMCC) | Truckee-Tahoe Airport (KTRK) | 2026-06-16 14:37 UTC | 2026-06-16 14:50 UTC | 13m |
| DESERT8 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-06-16 14:35 UTC | 2026-06-16 14:50 UTC | 15m |
| XBPBH | XBP | Hermanos Serdan International Airport (MMPB) | Tehuacan Airport (MMHC) | 2026-06-16 14:09 UTC | 2026-06-16 14:49 UTC | 39m |
| N470LP |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-06-16 13:44 UTC | 2026-06-16 14:46 UTC | 1h 1m |
| PREY21 | PRE | Randolph Afb Airport (KRND) | Bailey Airport (2TS8) | 2026-06-16 14:06 UTC | 2026-06-16 14:43 UTC | 37m |
| DFERD | DFE | Braunschweig Wolfsburg Airport (EDVE) | Siegerland Airport (EDGS) | 2026-06-16 13:49 UTC | 2026-06-16 14:43 UTC | 53m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
