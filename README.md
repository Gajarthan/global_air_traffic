# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--23_16:40:19_UTC-green)

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

**Latest saved flight:** 2026-07-23 16:40:19 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-23 16:40:19 UTC

- **145,831** saved flights
- **48,777** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **145,831** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,746,269.7 tonnes** estimated CO2 emissions
- **101,233,028 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5917 |
| 2 | SkyWest Airlines | 5328 |
| 3 | EJA | 2873 |
| 4 | IndiGo | 2643 |
| 5 | American Airlines | 2326 |
| 6 | Southwest Airlines | 2201 |
| 7 | ENY | 1812 |
| 8 | Delta Air Lines | 1724 |
| 9 | Lufthansa | 1449 |
| 10 | LATAM Airlines | 1344 |
| 11 | AZU | 1255 |
| 12 | Vueling | 1240 |
| 13 | WIF | 1240 |
| 14 | LXJ | 1122 |
| 15 | AXM | 1066 |
| 16 | Swiss International | 1032 |
| 17 | easyJet | 943 |
| 18 | All Nippon Airways | 932 |
| 19 | Alaska Airlines | 915 |
| 20 | QLK | 913 |
| 21 | EJU | 894 |
| 22 | VIV | 811 |
| 23 | CXK | 783 |
| 24 | AEE | 775 |
| 25 | JetBlue | 768 |
| 26 | Air France | 767 |
| 27 | MXY | 761 |
| 28 | Cathay Pacific | 758 |
| 29 | United Airlines | 756 |
| 30 | GLO | 749 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 125584 |
| 2 | 🇪🇸 ES | 9449 |
| 3 | 🇦🇺 AU | 8340 |
| 4 | 🇮🇳 IN | 8276 |
| 5 | 🇧🇷 BR | 8224 |
| 6 | 🇨🇦 CA | 7748 |
| 7 | 🇮🇹 IT | 7590 |
| 8 | 🇩🇪 DE | 7515 |
| 9 | 🇬🇧 GB | 6646 |
| 10 | 🇯🇵 JP | 6097 |
| 11 | 🇫🇷 FR | 5793 |
| 12 | 🇨🇴 CO | 4801 |
| 13 | 🇲🇽 MX | 4243 |
| 14 | 🇬🇷 GR | 4145 |
| 15 | 🇳🇴 NO | 3891 |
| 16 | 🇨🇭 CH | 3807 |
| 17 | 🇹🇷 TR | 3419 |
| 18 | 🇲🇾 MY | 2781 |
| 19 | 🇵🇱 PL | 2458 |
| 20 | 🇿🇦 ZA | 2372 |
| 21 | 🇳🇿 NZ | 2223 |
| 22 | 🇹🇭 TH | 2140 |
| 23 | 🇰🇷 KR | 2047 |
| 24 | 🇵🇭 PH | 1941 |
| 25 | 🇬🇹 GT | 1896 |
| 26 | 🇲🇦 MA | 1509 |
| 27 | 🇲🇪 ME | 1448 |
| 28 | 🇳🇱 NL | 1361 |
| 29 | 🇭🇷 HR | 1332 |
| 30 | 🇲🇴 MO | 1215 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3005 |
| 2 | Denver International Airport |  | US | 2438 |
| 3 | Tokyo International Airport |  | JP | 1959 |
| 4 | Indira Gandhi International Airport |  | IN | 1836 |
| 5 | Harry Reid International Airport |  | US | 1825 |
| 6 | Guaymaral Airport |  | CO | 1793 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1657 |
| 8 | Zurich Airport |  | CH | 1609 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1527 |
| 10 | La Aurora Airport |  | GT | 1469 |
| 11 | Frankfurt am Main International Airport |  | DE | 1400 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1372 |
| 13 | Chicago O'Hare International Airport |  | US | 1352 |
| 14 | Salt Lake City International Airport |  | US | 1308 |
| 15 | El Dorado International Airport |  | CO | 1306 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1264 |
| 17 | Macau International Airport |  | MO | 1215 |
| 18 | Capua Airport |  | IT | 1183 |
| 19 | Congonhas Airport |  | BR | 1171 |
| 20 | Madrid Barajas International Airport |  | ES | 1164 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1145 |
| 22 | Kuala Lumpur International Airport |  | MY | 1074 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1054 |
| 24 | Charlotte/Douglas International Airport |  | US | 1044 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1019 |
| 26 | Charles de Gaulle International Airport |  | FR | 1012 |
| 27 | Bengaluru International Airport |  | IN | 990 |
| 28 | Malpensa International Airport |  | IT | 941 |
| 29 | Ninoy Aquino International Airport |  | PH | 906 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 891 |
| 31 | Barcelona International Airport |  | ES | 883 |
| 32 | Daniel K Inouye International Airport |  | US | 879 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 869 |
| 34 | Tenerife Norte Airport |  | ES | 835 |
| 35 | Seattle-Tacoma International Airport |  | US | 829 |
| 36 | Viracopos International Airport |  | BR | 827 |
| 37 | Calgary International Airport |  | CA | 826 |
| 38 | Scottsdale Airport |  | US | 825 |
| 39 | Amsterdam Airport Schiphol |  | NL | 821 |
| 40 | Oslo Gardermoen Airport |  | NO | 804 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 755 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 528 | 21m | 244 km | 2,223.3 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 354 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 352 | 24m | 225 km | 1,365.6 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 345 | 1h 9m | 770 km | 4,583.1 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 289 | 1h 7m | 706 km | 3,518.6 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 262 | 26m | 275 km | 1,241.5 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 262 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 219 | 22m | 55 km | 208.2 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 195 | 1h 46m | 1,423 km | 4,785.6 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 195 | 44m | 241 km | 810.0 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 194 | 26m | 215 km | 718.5 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 192 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 190 | 20m | 99 km | 325.5 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 180 | 20m | 250 km | 777.5 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 180 | 28m | 152 km | 470.4 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 173 | 31m | 369 km | 1,101.2 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 173 | 18m | 144 km | 430.3 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 169 | 44m | 452 km | 1,317.1 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 168 | 1h 16m | 961 km | 2,784.7 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 166 | 1h 39m | 1,156 km | 3,311.6 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 166 | 1h 1m | 695 km | 1,989.8 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 165 | 13m | - | - |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 160 | 55m | 136 km | 375.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N77HD |  | Jonesboro Municipal Airport (KJBR) | Head Airfield (2AR7) | 2026-07-23 15:56 UTC | 2026-07-23 16:40 UTC | 44m |
| N797NA |  | Dubuque Regional Airport (KDBQ) | Dubuque Regional Airport (KDBQ) | 2026-07-23 15:45 UTC | 2026-07-23 16:33 UTC | 48m |
| N323Y |  | Jacksonville Executive At Craig Airport (KCRG) | Jekyll Island Airport (K09J) | 2026-07-23 16:17 UTC | 2026-07-23 16:32 UTC | 14m |
| N708LA |  | Northeast Philadelphia Airport (KPNE) | Lancaster Airport (KLNS) | 2026-07-23 15:49 UTC | 2026-07-23 16:31 UTC | 41m |
| N1233M |  | Wings On The Prairie Airport (2SD8) | Brookings Regional Airport (KBKX) | 2026-07-23 15:53 UTC | 2026-07-23 16:29 UTC | 36m |
| HBLVC | HBL | Leutkirch-Unterzeil Airport (EDNL) | Friedrichshafen Airport (EDNY) | 2026-07-23 15:56 UTC | 2026-07-23 16:26 UTC | 30m |
| SEUAL | SEU | Trollhattan-Vanersborg Airport (ESGT) | Satenas Air Base (ESIB) | 2026-07-23 16:10 UTC | 2026-07-23 16:24 UTC | 13m |
| N853CR |  | Long Beach (Daugherty Field) Airport (KLGB) | Meadows Field (KBFL) | 2026-07-23 15:43 UTC | 2026-07-23 16:23 UTC | 40m |
| N120BF |  | KU77 (KU77) | KU77 (KU77) | 2026-07-23 15:52 UTC | 2026-07-23 16:22 UTC | 29m |
| DESERT8 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-07-23 16:10 UTC | 2026-07-23 16:21 UTC | 10m |
| FAC5766 | FAC | El Dorado International Airport (SKBO) | Vanguardia Airport (SKVV) | 2026-07-23 16:04 UTC | 2026-07-23 16:18 UTC | 14m |
| CONGO63 | CON | Usaf Academy Davis Airfield (KAFF) | Usaf Academy Davis Airfield (KAFF) | 2026-07-23 15:51 UTC | 2026-07-23 16:17 UTC | 26m |
| N333CT |  | Ogden-Hinckley Airport (KOGD) | Malad City Airport (KMLD) | 2026-07-23 15:40 UTC | 2026-07-23 16:16 UTC | 36m |
| N404LH |  | Gold King Creek Airport (PAAN) | Gold King Creek Airport (PAAN) | 2026-07-23 16:12 UTC | 2026-07-23 16:13 UTC | 1m |
| N15KJ |  | William P Hobby Airport (KHOU) | Telluride Regional Airport (KTEX) | 2026-07-23 14:12 UTC | 2026-07-23 16:13 UTC | 2h 0m |
| TOPCT25 | TOP | Offutt Afb Airport (KOFF) | Hunt Field (SD47) | 2026-07-23 14:42 UTC | 2026-07-23 16:10 UTC | 1h 27m |
| EFY7834 | EFY | La Nubia Airport (SKMZ) | La Nubia Airport (SKMZ) | 2026-07-23 15:33 UTC | 2026-07-23 16:09 UTC | 36m |
| N513P |  | Martha's Vineyard Airport (KMVY) | Cape Cod Gateway Airport (KHYA) | 2026-07-23 15:04 UTC | 2026-07-23 16:08 UTC | 1h 3m |
| CAZ201 | CAZ | Firenze / Peretola Airport (LIRQ) | Sondrio Caiolo Airport (LILO) | 2026-07-23 15:35 UTC | 2026-07-23 16:07 UTC | 32m |
| N153PC |  | Falcon Field (KFFZ) | Montezuma Airport (19AZ) | 2026-07-23 15:28 UTC | 2026-07-23 16:07 UTC | 38m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
