# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--14_11:37:09_UTC-green)

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

**Latest saved flight:** 2026-07-14 11:37:09 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-14 11:37:09 UTC

- **141,438** saved flights
- **47,496** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **141,438** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,698,388.8 tonnes** estimated CO2 emissions
- **98,457,320 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5755 |
| 2 | SkyWest Airlines | 5175 |
| 3 | EJA | 2786 |
| 4 | IndiGo | 2587 |
| 5 | American Airlines | 2250 |
| 6 | Southwest Airlines | 2130 |
| 7 | ENY | 1756 |
| 8 | Delta Air Lines | 1675 |
| 9 | Lufthansa | 1430 |
| 10 | LATAM Airlines | 1298 |
| 11 | Vueling | 1217 |
| 12 | AZU | 1215 |
| 13 | WIF | 1214 |
| 14 | LXJ | 1086 |
| 15 | AXM | 1053 |
| 16 | Swiss International | 1008 |
| 17 | easyJet | 922 |
| 18 | All Nippon Airways | 909 |
| 19 | Alaska Airlines | 891 |
| 20 | QLK | 887 |
| 21 | EJU | 871 |
| 22 | VIV | 781 |
| 23 | AEE | 757 |
| 24 | CXK | 756 |
| 25 | Air France | 754 |
| 26 | JetBlue | 752 |
| 27 | United Airlines | 737 |
| 28 | Cathay Pacific | 732 |
| 29 | MXY | 731 |
| 30 | GLO | 724 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 121606 |
| 2 | 🇪🇸 ES | 9250 |
| 3 | 🇮🇳 IN | 8104 |
| 4 | 🇦🇺 AU | 8099 |
| 5 | 🇧🇷 BR | 7978 |
| 6 | 🇨🇦 CA | 7440 |
| 7 | 🇮🇹 IT | 7376 |
| 8 | 🇩🇪 DE | 7351 |
| 9 | 🇬🇧 GB | 6456 |
| 10 | 🇯🇵 JP | 5944 |
| 11 | 🇫🇷 FR | 5620 |
| 12 | 🇨🇴 CO | 4490 |
| 13 | 🇲🇽 MX | 4105 |
| 14 | 🇬🇷 GR | 4024 |
| 15 | 🇳🇴 NO | 3795 |
| 16 | 🇨🇭 CH | 3666 |
| 17 | 🇹🇷 TR | 3347 |
| 18 | 🇲🇾 MY | 2747 |
| 19 | 🇵🇱 PL | 2369 |
| 20 | 🇿🇦 ZA | 2314 |
| 21 | 🇳🇿 NZ | 2164 |
| 22 | 🇹🇭 TH | 2119 |
| 23 | 🇰🇷 KR | 2017 |
| 24 | 🇵🇭 PH | 1914 |
| 25 | 🇬🇹 GT | 1865 |
| 26 | 🇲🇦 MA | 1482 |
| 27 | 🇲🇪 ME | 1404 |
| 28 | 🇳🇱 NL | 1331 |
| 29 | 🇭🇷 HR | 1286 |
| 30 | 🇲🇴 MO | 1191 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2913 |
| 2 | Denver International Airport |  | US | 2363 |
| 3 | Tokyo International Airport |  | JP | 1921 |
| 4 | Indira Gandhi International Airport |  | IN | 1795 |
| 5 | Harry Reid International Airport |  | US | 1769 |
| 6 | Guaymaral Airport |  | CO | 1717 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1623 |
| 8 | Zurich Airport |  | CH | 1575 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1484 |
| 10 | La Aurora Airport |  | GT | 1442 |
| 11 | Frankfurt am Main International Airport |  | DE | 1380 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1347 |
| 13 | Chicago O'Hare International Airport |  | US | 1328 |
| 14 | Salt Lake City International Airport |  | US | 1264 |
| 15 | El Dorado International Airport |  | CO | 1248 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1229 |
| 17 | Macau International Airport |  | MO | 1191 |
| 18 | Capua Airport |  | IT | 1158 |
| 19 | Madrid Barajas International Airport |  | ES | 1143 |
| 20 | Congonhas Airport |  | BR | 1135 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1127 |
| 22 | Kuala Lumpur International Airport |  | MY | 1060 |
| 23 | Charlotte/Douglas International Airport |  | US | 1027 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1024 |
| 25 | Charles de Gaulle International Airport |  | FR | 999 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 985 |
| 27 | Bengaluru International Airport |  | IN | 970 |
| 28 | Malpensa International Airport |  | IT | 918 |
| 29 | Ninoy Aquino International Airport |  | PH | 893 |
| 30 | Daniel K Inouye International Airport |  | US | 864 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 864 |
| 32 | Barcelona International Airport |  | ES | 861 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 833 |
| 34 | Tenerife Norte Airport |  | ES | 820 |
| 35 | Calgary International Airport |  | CA | 811 |
| 36 | Viracopos International Airport |  | BR | 802 |
| 37 | Seattle-Tacoma International Airport |  | US | 802 |
| 38 | Amsterdam Airport Schiphol |  | NL | 801 |
| 39 | Scottsdale Airport |  | US | 801 |
| 40 | Vitoria/Foronda Airport |  | ES | 781 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 724 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 514 | 21m | 244 km | 2,164.3 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 345 | 24m | 225 km | 1,338.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 345 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 335 | 1h 9m | 770 km | 4,450.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 298 | 14m | 114 km | 584.5 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 258 | 26m | 275 km | 1,222.6 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 254 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 207 | 22m | 55 km | 196.7 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 191 | 26m | 215 km | 707.4 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 190 | 1h 46m | 1,423 km | 4,662.9 t |
| 16 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 190 | 44m | 241 km | 789.2 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 189 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 189 | 20m | 99 km | 323.7 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 177 | 28m | 152 km | 462.6 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 176 | 20m | 250 km | 760.2 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 172 | 31m | 369 km | 1,094.8 t |
| 22 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 170 | 18m | 144 km | 422.9 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 165 | 44m | 452 km | 1,285.9 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 163 | 1h 16m | 961 km | 2,701.8 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 162 | 1h 38m | 1,156 km | 3,231.8 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 162 | 1h 1m | 695 km | 1,941.9 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 158 | 13m | - | - |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 157 | 54m | 136 km | 368.1 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 156 | 14m | 154 km | 413.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| JIA5088 | JIA | Norfolk International Airport (KORF) | Philadelphia International Airport (KPHL) | 2026-07-14 10:33 UTC | 2026-07-14 11:37 UTC | 1h 3m |
| RYR99GJ | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | Olbia / Costa Smeralda Airport (LIEO) | 2026-07-14 10:50 UTC | 2026-07-14 11:35 UTC | 45m |
| N278FG |  | Trenton Mercer Airport (KTTN) | Sky Manor Airport (KN40) | 2026-07-14 10:49 UTC | 2026-07-14 11:23 UTC | 34m |
| N734VQ |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-07-14 10:49 UTC | 2026-07-14 11:15 UTC | 25m |
| TSIOO | TSI | Tunis Carthage International Airport (DTTA) | Tunis Carthage International Airport (DTTA) | 2026-07-14 11:04 UTC | 2026-07-14 11:06 UTC | 1m |
| WIF5WP | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-07-14 10:53 UTC | 2026-07-14 11:04 UTC | 10m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-07-14 10:44 UTC | 2026-07-14 11:01 UTC | 17m |
| FVS443 | FVS | Futaysi Airport (OMAF) | OM10 (OM10) | 2026-07-14 10:36 UTC | 2026-07-14 11:01 UTC | 24m |
| N4065Q |  | Harford County Airport (K0W3) | Ocean City Municipal Airport (KOXB) | 2026-07-14 10:13 UTC | 2026-07-14 10:57 UTC | 44m |
| OEAET | OEA | Medulin Campanoz Airport (LDPM) | Medulin Campanoz Airport (LDPM) | 2026-07-14 10:45 UTC | 2026-07-14 10:56 UTC | 11m |
| JANET11 | JAN | Harry Reid International Airport (KLAS) | NV11 (NV11) | 2026-07-14 10:42 UTC | 2026-07-14 10:54 UTC | 12m |
| OC61 |  | Nagasaki Airport (RJFU) | Iki Airport (RJDB) | 2026-07-14 10:37 UTC | 2026-07-14 10:49 UTC | 11m |
| RYR9CE | Ryanair | Marseille Provence Airport (LFML) | Tours-Val-de-Loire Airport (LFOT) | 2026-07-14 09:53 UTC | 2026-07-14 10:48 UTC | 54m |
| RYR99PN | Ryanair | Budapest Ferenc Liszt International Airport (LHBP) | Otocac Airport (LDRO) | 2026-07-14 10:10 UTC | 2026-07-14 10:48 UTC | 37m |
| JBU207 | JetBlue | Presque Isle International Airport (KPQI) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-14 09:56 UTC | 2026-07-14 10:47 UTC | 51m |
| UPS844 | UPS | Louisville Muhammad Ali International Airport (KSDF) | Salt Lake City International Airport (KSLC) | 2026-07-14 07:53 UTC | 2026-07-14 10:44 UTC | 2h 51m |
| AIC1775 | Air India | Indira Gandhi International Airport (VIDP) | Sarsawa Air Force Station (VISP) | 2026-07-14 10:23 UTC | 2026-07-14 10:43 UTC | 20m |
| JAL377 | Japan Airlines | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-07-14 09:42 UTC | 2026-07-14 10:42 UTC | 1h 0m |
| UIA8712 | UIA | Wang-an Airport (RCWA) | Kaohsiung International Airport (RCKH) | 2026-07-14 10:20 UTC | 2026-07-14 10:42 UTC | 21m |
| MGETS | MGE | RAF Church Fenton (EGXG) | Guernsey Airport (EGJB) | 2026-07-14 09:24 UTC | 2026-07-14 10:41 UTC | 1h 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
