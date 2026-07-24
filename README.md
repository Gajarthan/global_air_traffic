# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--24_11:56:00_UTC-green)

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

**Latest saved flight:** 2026-07-24 11:56:00 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-24 11:56:00 UTC

- **147,477** saved flights
- **49,251** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **147,477** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,766,442.3 tonnes** estimated CO2 emissions
- **102,402,451 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5967 |
| 2 | SkyWest Airlines | 5402 |
| 3 | EJA | 2914 |
| 4 | IndiGo | 2655 |
| 5 | American Airlines | 2348 |
| 6 | Southwest Airlines | 2230 |
| 7 | ENY | 1833 |
| 8 | Delta Air Lines | 1746 |
| 9 | Lufthansa | 1451 |
| 10 | LATAM Airlines | 1356 |
| 11 | AZU | 1274 |
| 12 | WIF | 1254 |
| 13 | Vueling | 1249 |
| 14 | LXJ | 1134 |
| 15 | AXM | 1071 |
| 16 | Swiss International | 1047 |
| 17 | easyJet | 951 |
| 18 | All Nippon Airways | 937 |
| 19 | Alaska Airlines | 926 |
| 20 | QLK | 922 |
| 21 | EJU | 900 |
| 22 | VIV | 820 |
| 23 | CXK | 789 |
| 24 | AEE | 779 |
| 25 | Air France | 773 |
| 26 | Cathay Pacific | 773 |
| 27 | JetBlue | 773 |
| 28 | MXY | 770 |
| 29 | United Airlines | 765 |
| 30 | GLO | 763 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 127138 |
| 2 | 🇪🇸 ES | 9536 |
| 3 | 🇦🇺 AU | 8449 |
| 4 | 🇮🇳 IN | 8333 |
| 5 | 🇧🇷 BR | 8326 |
| 6 | 🇨🇦 CA | 7888 |
| 7 | 🇮🇹 IT | 7653 |
| 8 | 🇩🇪 DE | 7562 |
| 9 | 🇬🇧 GB | 6727 |
| 10 | 🇯🇵 JP | 6153 |
| 11 | 🇫🇷 FR | 5847 |
| 12 | 🇨🇴 CO | 4881 |
| 13 | 🇲🇽 MX | 4284 |
| 14 | 🇬🇷 GR | 4177 |
| 15 | 🇳🇴 NO | 3932 |
| 16 | 🇨🇭 CH | 3853 |
| 17 | 🇹🇷 TR | 3459 |
| 18 | 🇲🇾 MY | 2790 |
| 19 | 🇵🇱 PL | 2487 |
| 20 | 🇿🇦 ZA | 2382 |
| 21 | 🇳🇿 NZ | 2243 |
| 22 | 🇹🇭 TH | 2164 |
| 23 | 🇰🇷 KR | 2055 |
| 24 | 🇵🇭 PH | 1975 |
| 25 | 🇬🇹 GT | 1908 |
| 26 | 🇲🇦 MA | 1515 |
| 27 | 🇲🇪 ME | 1459 |
| 28 | 🇳🇱 NL | 1370 |
| 29 | 🇭🇷 HR | 1343 |
| 30 | 🇲🇴 MO | 1232 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3035 |
| 2 | Denver International Airport |  | US | 2470 |
| 3 | Tokyo International Airport |  | JP | 1972 |
| 4 | Indira Gandhi International Airport |  | IN | 1849 |
| 5 | Harry Reid International Airport |  | US | 1839 |
| 6 | Guaymaral Airport |  | CO | 1814 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1663 |
| 8 | Zurich Airport |  | CH | 1626 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1551 |
| 10 | La Aurora Airport |  | GT | 1479 |
| 11 | Frankfurt am Main International Airport |  | DE | 1402 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1388 |
| 13 | Chicago O'Hare International Airport |  | US | 1367 |
| 14 | Salt Lake City International Airport |  | US | 1329 |
| 15 | El Dorado International Airport |  | CO | 1320 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1274 |
| 17 | Macau International Airport |  | MO | 1232 |
| 18 | Capua Airport |  | IT | 1193 |
| 19 | Congonhas Airport |  | BR | 1187 |
| 20 | Madrid Barajas International Airport |  | ES | 1173 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1153 |
| 22 | Kuala Lumpur International Airport |  | MY | 1075 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1065 |
| 24 | Charlotte/Douglas International Airport |  | US | 1050 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1033 |
| 26 | Charles de Gaulle International Airport |  | FR | 1020 |
| 27 | Bengaluru International Airport |  | IN | 995 |
| 28 | Malpensa International Airport |  | IT | 952 |
| 29 | Ninoy Aquino International Airport |  | PH | 924 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 903 |
| 31 | Barcelona International Airport |  | ES | 890 |
| 32 | Daniel K Inouye International Airport |  | US | 886 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 884 |
| 34 | Seattle-Tacoma International Airport |  | US | 847 |
| 35 | Tenerife Norte Airport |  | ES | 845 |
| 36 | Calgary International Airport |  | CA | 844 |
| 37 | Viracopos International Airport |  | BR | 835 |
| 38 | Scottsdale Airport |  | US | 833 |
| 39 | Amsterdam Airport Schiphol |  | NL | 826 |
| 40 | Oslo Gardermoen Airport |  | NO | 814 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 765 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 535 | 21m | 244 km | 2,252.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 360 | 24m | 225 km | 1,396.6 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 356 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 346 | 1h 9m | 770 km | 4,596.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 289 | 1h 7m | 706 km | 3,518.6 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 265 | 27m | 275 km | 1,255.7 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 265 | 32m | - | - |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 222 | 22m | 55 km | 211.0 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 200 | 44m | 241 km | 830.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 198 | 1h 46m | 1,423 km | 4,859.2 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 195 | 26m | 215 km | 722.2 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 195 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 190 | 20m | 99 km | 325.5 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 180 | 20m | 250 km | 777.5 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 180 | 28m | 152 km | 470.4 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 175 | 31m | 369 km | 1,113.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 174 | 18m | 144 km | 432.8 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 172 | 1h 16m | 961 km | 2,851.0 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 171 | 12m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 170 | 44m | 452 km | 1,324.9 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 168 | 1h 1m | 695 km | 2,013.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 166 | 1h 39m | 1,156 km | 3,311.6 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 161 | 55m | 136 km | 377.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N139ER |  | Newport News/Williamsburg International Airport (KPHF) | Richmond Executive/Chesterfield County Airport (KFCI) | 2026-07-24 11:17 UTC | 2026-07-24 11:56 UTC | 38m |
| N257EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-07-24 10:53 UTC | 2026-07-24 11:55 UTC | 1h 2m |
| CXK1076 | CXK | City Of Colorado Springs Municipal Airport (KCOS) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-07-24 11:34 UTC | 2026-07-24 11:51 UTC | 17m |
| N116FA |  | Riley Field (4IN7) | Riley Field (4IN7) | 2026-07-24 11:12 UTC | 2026-07-24 11:38 UTC | 25m |
| N35TJ |  | Youngstown Elser Metro Airport (K4G4) | Bieber Field (4OH3) | 2026-07-24 11:24 UTC | 2026-07-24 11:34 UTC | 10m |
| HK5463X |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-07-24 11:23 UTC | 2026-07-24 11:27 UTC | 3m |
| SWU1947 | SWU | Kefallinia Airport (LGKF) | Trento / Mattarello Airport (LIDT) | 2026-07-24 08:57 UTC | 2026-07-24 11:16 UTC | 2h 19m |
| PLF106 | PLF | Szczecin-Goleniow Solidarność Airport (EPSC) | Rzeszow-Jasionka Airport (EPRZ) | 2026-07-24 10:17 UTC | 2026-07-24 11:15 UTC | 57m |
| EZS52WA | EZS | Eleftherios Venizelos International Airport (LGAV) | Mollis Airport (LSZM) | 2026-07-24 08:30 UTC | 2026-07-24 11:12 UTC | 2h 42m |
| EZS72LT | EZS | Mollis Airport (LSZM) | Mollis Airport (LSZM) | 2026-07-24 10:51 UTC | 2026-07-24 11:10 UTC | 18m |
| EIN503 | Aer Lingus | Bordeaux-Merignac (BA 106) Airport (LFBD) | Dublin Airport (EIDW) | 2026-07-24 09:35 UTC | 2026-07-24 11:01 UTC | 1h 25m |
| SEH4JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Kalymnos Airport (LGKY) | 2026-07-24 10:35 UTC | 2026-07-24 11:01 UTC | 25m |
| HNL47B | HNL | De Kooy Airport (EHKD) | Beccles Airport (EGSM) | 2026-07-24 10:12 UTC | 2026-07-24 10:58 UTC | 46m |
| CHX22 | CHX | Erbach Airport (EDNE) | Blaubeuren Airport (EDMC) | 2026-07-24 10:53 UTC | 2026-07-24 10:57 UTC | 3m |
| TAM3474 | LATAM Airlines | Congonhas Airport (SBSP) | Fazenda Santa Thereza Airport (SNZL) | 2026-07-24 10:15 UTC | 2026-07-24 10:57 UTC | 42m |
| WIF5WP | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-07-24 10:47 UTC | 2026-07-24 10:56 UTC | 9m |
| AE921 |  | Sydney Bankstown Airport (YSBK) | Bathurst Airport (YBTH) | 2026-07-24 10:35 UTC | 2026-07-24 10:56 UTC | 20m |
| LLR513 | LLR | Bengaluru International Airport (VOBL) | Hosur Airport (VO95) | 2026-07-24 10:33 UTC | 2026-07-24 10:53 UTC | 20m |
| N160AM |  | Lake Arrowhead Airport (2CN8) | Big Bear City Airport (KL35) | 2026-07-24 10:44 UTC | 2026-07-24 10:52 UTC | 7m |
| AHY8042 | AHY | Gaziemir Airport (LTBK) | Sivas Airport (LTAR) | 2026-07-24 09:54 UTC | 2026-07-24 10:52 UTC | 58m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
